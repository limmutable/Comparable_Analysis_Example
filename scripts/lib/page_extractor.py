"""
PDF page extractor for creating smaller text files.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

from .config import Config, DEFAULT_CONFIG


@dataclass
class ExtractionResult:
    """Result of a page extraction operation."""
    success: bool
    source_path: Path
    output_path: Optional[Path] = None
    pages_extracted: int = 0
    start_page: int = 0
    end_page: int = 0
    text_size: int = 0
    estimated_tokens: int = 0
    error_message: Optional[str] = None

    @property
    def page_range(self) -> str:
        """Human-readable page range."""
        return f"{self.start_page}-{self.end_page}"

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "success": self.success,
            "source_path": str(self.source_path),
            "output_path": str(self.output_path) if self.output_path else None,
            "pages_extracted": self.pages_extracted,
            "page_range": self.page_range,
            "text_size": self.text_size,
            "estimated_tokens": self.estimated_tokens,
            "error_message": self.error_message,
        }


class PageExtractor:
    """Extract pages from PDF files to text."""

    def __init__(self, config: Optional[Config] = None):
        """
        Initialize page extractor.

        Args:
            config: Configuration object. Uses DEFAULT_CONFIG if not provided.
        """
        self.config = config or DEFAULT_CONFIG

        if not HAS_PYPDF2:
            raise ImportError(
                "PyPDF2 is required for PDF extraction. "
                "Install with: pip install PyPDF2"
            )

    def get_page_count(self, pdf_path: Path) -> int:
        """
        Get total page count of a PDF.

        Args:
            pdf_path: Path to PDF file.

        Returns:
            Number of pages in the PDF.
        """
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return len(reader.pages)

    def generate_output_path(
        self,
        source_path: Path,
        start_page: int,
        end_page: int,
        company: Optional[str] = None
    ) -> Path:
        """
        Generate output path for extracted text.

        Args:
            source_path: Path to source PDF.
            start_page: First page (1-indexed).
            end_page: Last page (1-indexed).
            company: Company name for subdirectory. Auto-detected if None.

        Returns:
            Path to output text file.
        """
        if company is None:
            company = source_path.parent.name

        filename = source_path.stem
        output_filename = f"{filename}-{start_page}-{end_page}.txt"

        output_dir = self.config.get_working_path() / company
        return output_dir / output_filename

    def extract_pages(
        self,
        pdf_path: Path,
        start_page: int,
        end_page: int,
        output_path: Optional[Path] = None,
        company: Optional[str] = None
    ) -> ExtractionResult:
        """
        Extract a range of pages from a PDF to text.

        Args:
            pdf_path: Path to source PDF.
            start_page: First page to extract (1-indexed).
            end_page: Last page to extract (1-indexed).
            output_path: Path to output file. Auto-generated if None.
            company: Company name for subdirectory.

        Returns:
            ExtractionResult with details of the operation.
        """
        pdf_path = Path(pdf_path)

        # Validate inputs
        if not pdf_path.exists():
            return ExtractionResult(
                success=False,
                source_path=pdf_path,
                error_message=f"Source file not found: {pdf_path}"
            )

        try:
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                total_pages = len(reader.pages)

                # Validate page range
                if start_page < 1:
                    start_page = 1
                if end_page > total_pages:
                    end_page = total_pages
                if start_page > end_page:
                    return ExtractionResult(
                        success=False,
                        source_path=pdf_path,
                        start_page=start_page,
                        end_page=end_page,
                        error_message=f"Invalid page range: {start_page}-{end_page}"
                    )

                # Convert to 0-indexed
                start_idx = start_page - 1
                end_idx = end_page

                # Extract text
                text_parts = []
                for i in range(start_idx, end_idx):
                    page = reader.pages[i]
                    text = page.extract_text() or ""
                    text_parts.append(f"\n--- Page {i + 1} ---\n\n{text}")

                full_text = "\n".join(text_parts)

                # Generate output path if not provided
                if output_path is None:
                    output_path = self.generate_output_path(
                        pdf_path, start_page, end_page, company
                    )

                output_path = Path(output_path)

                # Create output directory
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Write output
                with open(output_path, 'w', encoding='utf-8') as out:
                    out.write(full_text)

                text_size = len(full_text)
                estimated_tokens = int(text_size / self.config.bytes_per_token_text)

                return ExtractionResult(
                    success=True,
                    source_path=pdf_path,
                    output_path=output_path,
                    pages_extracted=end_page - start_page + 1,
                    start_page=start_page,
                    end_page=end_page,
                    text_size=text_size,
                    estimated_tokens=estimated_tokens
                )

        except Exception as e:
            return ExtractionResult(
                success=False,
                source_path=pdf_path,
                start_page=start_page,
                end_page=end_page,
                error_message=str(e)
            )

    def extract_multiple_ranges(
        self,
        pdf_path: Path,
        page_ranges: List[Tuple[int, int]],
        company: Optional[str] = None
    ) -> List[ExtractionResult]:
        """
        Extract multiple page ranges from a PDF.

        Args:
            pdf_path: Path to source PDF.
            page_ranges: List of (start, end) tuples.
            company: Company name for subdirectory.

        Returns:
            List of ExtractionResult objects.
        """
        results = []
        for start, end in page_ranges:
            result = self.extract_pages(pdf_path, start, end, company=company)
            results.append(result)
        return results

    def extract_for_analysis(
        self,
        pdf_path: Path,
        company: Optional[str] = None,
        filing_type: str = "10k"
    ) -> List[ExtractionResult]:
        """
        Extract standard page ranges for financial analysis.

        Args:
            pdf_path: Path to source PDF.
            company: Company name for subdirectory.
            filing_type: Type of filing ("10k" or "korean_sec").

        Returns:
            List of ExtractionResult objects.
        """
        if filing_type == "korean_sec":
            page_ranges = self.config.korean_sec_page_ranges
        else:
            page_ranges = self.config.default_page_ranges

        # Adjust ranges based on actual page count
        total_pages = self.get_page_count(pdf_path)
        adjusted_ranges = [
            (start, min(end, total_pages))
            for start, end in page_ranges
            if start <= total_pages
        ]

        return self.extract_multiple_ranges(pdf_path, adjusted_ranges, company)
