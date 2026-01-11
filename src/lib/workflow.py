"""
High-level workflow orchestration for document preparation.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

from .config import Config, DEFAULT_CONFIG
from .document_checker import DocumentChecker, FileInfo, FileStatus
from .page_extractor import PageExtractor, ExtractionResult


@dataclass
class WorkflowResult:
    """Result of a complete preparation workflow."""
    company: str
    success: bool
    source_files: List[FileInfo] = field(default_factory=list)
    working_files: List[FileInfo] = field(default_factory=list)
    extractions: List[ExtractionResult] = field(default_factory=list)
    needs_extraction: bool = False
    extraction_performed: bool = False
    error_message: Optional[str] = None

    @property
    def total_working_tokens(self) -> int:
        """Total estimated tokens in working files."""
        return sum(f.estimated_tokens for f in self.working_files)

    @property
    def files_ready(self) -> List[str]:
        """List of files ready for analysis."""
        return [str(f.path) for f in self.working_files if f.is_ok]

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "company": self.company,
            "success": self.success,
            "source_files": [f.to_dict() for f in self.source_files],
            "working_files": [f.to_dict() for f in self.working_files],
            "extractions": [e.to_dict() for e in self.extractions],
            "needs_extraction": self.needs_extraction,
            "extraction_performed": self.extraction_performed,
            "total_working_tokens": self.total_working_tokens,
            "files_ready": self.files_ready,
            "error_message": self.error_message,
        }

    def format_report(self) -> str:
        """Format a human-readable report."""
        lines = [
            f"## Document Preparation: {self.company}",
            "",
        ]

        # Source files
        if self.source_files:
            lines.append("### Source Files (dataroom/)")
            lines.append("")
            lines.append("| File | Size | Tokens | Status |")
            lines.append("|------|------|--------|--------|")
            for f in self.source_files:
                status_icon = {
                    FileStatus.OK: "✓",
                    FileStatus.WARNING: "⚠️",
                    FileStatus.TOO_LARGE: "❌",
                    FileStatus.NOT_FOUND: "?",
                    FileStatus.ERROR: "!",
                }.get(f.status, "?")
                lines.append(
                    f"| {f.path.name} | {f.size_mb:.1f} MB | {f.tokens_k:.0f}K | {status_icon} {f.status.value} |"
                )
            lines.append("")

        # Working files
        if self.working_files:
            lines.append("### Working Files (.working/)")
            lines.append("")
            lines.append("| File | Size | Tokens |")
            lines.append("|------|------|--------|")
            for f in self.working_files:
                lines.append(
                    f"| {f.path.name} | {f.size_kb:.1f} KB | {f.tokens_k:.0f}K |"
                )
            lines.append("")
            lines.append(f"**Total tokens:** ~{self.total_working_tokens / 1000:.0f}K")
            lines.append("")

        # Extractions performed
        if self.extractions:
            lines.append("### Extractions Performed")
            lines.append("")
            for e in self.extractions:
                if e.success:
                    lines.append(
                        f"- Pages {e.page_range} → {e.output_path.name} "
                        f"({e.estimated_tokens / 1000:.0f}K tokens)"
                    )
                else:
                    lines.append(f"- Pages {e.page_range} → FAILED: {e.error_message}")
            lines.append("")

        # Next steps
        lines.append("### Next Steps")
        lines.append("")
        if self.working_files:
            lines.append("Files are ready for analysis. Use one of these commands:")
            lines.append("")
            lines.append("```bash")
            lines.append("# With Gemini CLI")
            lines.append("gemini")
            lines.append(f'> "Read {self.working_files[0].path} and summarize the company"')
            lines.append("")
            lines.append("# With Claude Code")
            lines.append("claude")
            lines.append(f'> "Analyze {self.company} using files in .working/{self.company}/"')
            lines.append("```")
        else:
            lines.append("No working files available. Run extraction first.")

        return "\n".join(lines)


class PrepWorkflow:
    """Orchestrate document preparation workflow."""

    def __init__(self, config: Optional[Config] = None):
        """
        Initialize workflow.

        Args:
            config: Configuration object. Uses DEFAULT_CONFIG if not provided.
        """
        self.config = config or DEFAULT_CONFIG
        self.checker = DocumentChecker(self.config)
        self.extractor = PageExtractor(self.config)

    def check_company(self, company: str) -> WorkflowResult:
        """
        Check a company's documents without extracting.

        Args:
            company: Company name/directory.

        Returns:
            WorkflowResult with current status.
        """
        source_files = self.checker.find_company_files(company)
        working_files = self.checker.find_working_files(company)
        needs_extraction = any(f.is_too_large for f in source_files) and not working_files

        return WorkflowResult(
            company=company,
            success=True,
            source_files=source_files,
            working_files=working_files,
            needs_extraction=needs_extraction,
            extraction_performed=False,
        )

    def prepare_company(
        self,
        company: str,
        force: bool = False,
        filing_type: str = "auto"
    ) -> WorkflowResult:
        """
        Prepare a company's documents for analysis.

        Checks existing files, extracts if needed.

        Args:
            company: Company name/directory.
            force: Force re-extraction even if working files exist.
            filing_type: "10k", "korean_sec", or "auto" (detect from filename).

        Returns:
            WorkflowResult with preparation status.
        """
        # Check existing files
        source_files = self.checker.find_company_files(company)
        working_files = self.checker.find_working_files(company)

        # If no source files, nothing to do
        if not source_files:
            return WorkflowResult(
                company=company,
                success=False,
                error_message=f"No PDF files found in dataroom/{company}/"
            )

        # Check if extraction is needed
        has_large_files = any(f.is_too_large for f in source_files)
        has_working_files = len(working_files) > 0

        needs_extraction = has_large_files and (not has_working_files or force)

        extractions = []

        if needs_extraction:
            # Extract from each large PDF
            for source in source_files:
                if not source.is_too_large and not force:
                    continue

                # Auto-detect filing type
                detected_type = filing_type
                if filing_type == "auto":
                    filename = source.path.name.lower()
                    if "sec" in filename or "신고" in filename:
                        detected_type = "korean_sec"
                    else:
                        detected_type = "10k"

                # Extract pages
                results = self.extractor.extract_for_analysis(
                    source.path,
                    company=company,
                    filing_type=detected_type
                )
                extractions.extend(results)

            # Re-check working files after extraction
            working_files = self.checker.find_working_files(company)

        return WorkflowResult(
            company=company,
            success=True,
            source_files=source_files,
            working_files=working_files,
            extractions=extractions,
            needs_extraction=needs_extraction,
            extraction_performed=len(extractions) > 0,
        )

    def extract_pages(
        self,
        company: str,
        start_page: int,
        end_page: int,
        source_file: Optional[str] = None
    ) -> ExtractionResult:
        """
        Extract specific pages from a company's PDF.

        Args:
            company: Company name/directory.
            start_page: First page (1-indexed).
            end_page: Last page (1-indexed).
            source_file: Specific PDF filename. Uses first PDF if None.

        Returns:
            ExtractionResult with extraction details.
        """
        source_files = self.checker.find_company_files(company)

        if not source_files:
            return ExtractionResult(
                success=False,
                source_path=Path(f"dataroom/{company}/"),
                error_message=f"No PDF files found in dataroom/{company}/"
            )

        # Find the right source file
        if source_file:
            matching = [f for f in source_files if f.path.name == source_file]
            if not matching:
                return ExtractionResult(
                    success=False,
                    source_path=Path(f"dataroom/{company}/{source_file}"),
                    error_message=f"File not found: {source_file}"
                )
            pdf_path = matching[0].path
        else:
            pdf_path = source_files[0].path

        return self.extractor.extract_pages(
            pdf_path,
            start_page,
            end_page,
            company=company
        )
