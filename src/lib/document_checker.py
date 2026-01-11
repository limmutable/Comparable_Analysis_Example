"""
Document size checker for estimating token counts.
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional

from .config import Config, DEFAULT_CONFIG


class FileStatus(Enum):
    """Status of a file based on token count."""
    OK = "ok"
    WARNING = "warning"
    TOO_LARGE = "too_large"
    NOT_FOUND = "not_found"
    ERROR = "error"


@dataclass
class FileInfo:
    """Information about a file including size and token estimates."""
    path: Path
    exists: bool
    size_bytes: int = 0
    estimated_tokens: int = 0
    status: FileStatus = FileStatus.OK
    error_message: Optional[str] = None

    @property
    def size_mb(self) -> float:
        """Size in megabytes."""
        return self.size_bytes / (1024 * 1024)

    @property
    def size_kb(self) -> float:
        """Size in kilobytes."""
        return self.size_bytes / 1024

    @property
    def tokens_k(self) -> float:
        """Estimated tokens in thousands."""
        return self.estimated_tokens / 1000

    @property
    def is_ok(self) -> bool:
        """Check if file is within safe limits."""
        return self.status == FileStatus.OK

    @property
    def is_too_large(self) -> bool:
        """Check if file exceeds safe limits."""
        return self.status == FileStatus.TOO_LARGE

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "path": str(self.path),
            "exists": self.exists,
            "size_bytes": self.size_bytes,
            "size_mb": round(self.size_mb, 2),
            "estimated_tokens": self.estimated_tokens,
            "status": self.status.value,
            "error_message": self.error_message,
        }


class DocumentChecker:
    """Check document sizes and estimate token counts."""

    def __init__(self, config: Optional[Config] = None):
        """
        Initialize document checker.

        Args:
            config: Configuration object. Uses DEFAULT_CONFIG if not provided.
        """
        self.config = config or DEFAULT_CONFIG

    def estimate_tokens(self, file_path: Path) -> int:
        """
        Estimate token count for a file.

        Args:
            file_path: Path to the file.

        Returns:
            Estimated token count.
        """
        if not file_path.exists():
            return 0

        size_bytes = file_path.stat().st_size
        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            bytes_per_token = self.config.bytes_per_token_pdf
        else:
            bytes_per_token = self.config.bytes_per_token_text

        return int(size_bytes / bytes_per_token)

    def get_status(self, tokens: int) -> FileStatus:
        """
        Determine file status based on token count.

        Args:
            tokens: Estimated token count.

        Returns:
            FileStatus enum value.
        """
        if tokens > self.config.safe_token_limit:
            return FileStatus.TOO_LARGE
        elif tokens > self.config.warning_token_limit:
            return FileStatus.WARNING
        return FileStatus.OK

    def check_file(self, file_path: Path) -> FileInfo:
        """
        Check a single file and return its info.

        Args:
            file_path: Path to the file.

        Returns:
            FileInfo object with size and status.
        """
        path = Path(file_path)

        if not path.exists():
            return FileInfo(
                path=path,
                exists=False,
                status=FileStatus.NOT_FOUND,
                error_message=f"File not found: {path}"
            )

        try:
            size_bytes = path.stat().st_size
            tokens = self.estimate_tokens(path)
            status = self.get_status(tokens)

            return FileInfo(
                path=path,
                exists=True,
                size_bytes=size_bytes,
                estimated_tokens=tokens,
                status=status
            )
        except Exception as e:
            return FileInfo(
                path=path,
                exists=True,
                status=FileStatus.ERROR,
                error_message=str(e)
            )

    def check_directory(self, dir_path: Path, pattern: str = "*.pdf") -> List[FileInfo]:
        """
        Check all matching files in a directory.

        Args:
            dir_path: Path to directory.
            pattern: Glob pattern for files to check.

        Returns:
            List of FileInfo objects.
        """
        path = Path(dir_path)
        if not path.exists() or not path.is_dir():
            return []

        files = sorted(path.glob(pattern))
        return [self.check_file(f) for f in files]

    def find_company_files(self, company: str) -> List[FileInfo]:
        """
        Find all PDF files for a company in the dataroom.

        Args:
            company: Company name/directory.

        Returns:
            List of FileInfo objects for company PDFs.
        """
        company_dir = self.config.get_dataroom_path() / company
        return self.check_directory(company_dir, "*.pdf")

    def find_working_files(self, company: str) -> List[FileInfo]:
        """
        Find all extracted text files for a company in .working/.

        Args:
            company: Company name/directory.

        Returns:
            List of FileInfo objects for extracted text files.
        """
        working_dir = self.config.get_working_path() / company
        return self.check_directory(working_dir, "*.txt")

    def needs_extraction(self, company: str) -> bool:
        """
        Check if a company's documents need extraction.

        Returns True if:
        - Source PDFs exist and are too large
        - No working files exist yet

        Args:
            company: Company name/directory.

        Returns:
            True if extraction is needed.
        """
        source_files = self.find_company_files(company)
        working_files = self.find_working_files(company)

        # If no source files, nothing to extract
        if not source_files:
            return False

        # If working files exist, extraction might not be needed
        if working_files:
            return False

        # Check if any source file is too large
        return any(f.is_too_large for f in source_files)
