"""
Configuration constants for document preparation.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple


@dataclass
class Config:
    """Configuration for document preparation workflow."""

    # Token estimation
    bytes_per_token_pdf: float = 4.5
    bytes_per_token_text: float = 4.0

    # Token limits
    safe_token_limit: int = 500_000  # Safe limit for most LLMs
    warning_token_limit: int = 200_000  # Start warning at this level

    # Directory paths (relative to project root)
    dataroom_dir: str = "dataroom"
    working_dir: str = ".working"
    output_dir: str = "output"

    # Default page ranges for 10-K / SEC filings
    default_page_ranges: List[Tuple[int, int]] = field(default_factory=lambda: [
        (1, 30),      # Cover, TOC, Business overview
        (45, 60),     # Selected financial data (Item 6)
        (80, 130),    # Financial statements (Item 8)
        (150, 200),   # Risk factors, detailed financials
    ])

    # Korean SEC filing (증권신고서) page ranges
    korean_sec_page_ranges: List[Tuple[int, int]] = field(default_factory=lambda: [
        (1, 30),      # 표지, 목차
        (100, 150),   # 사업 내용
        (150, 200),   # 재무 정보 (1)
        (200, 250),   # 재무 정보 (2)
        (250, 320),   # 투자위험요소
    ])

    def get_project_root(self) -> Path:
        """Get project root directory."""
        # Assume we're running from project root or scripts/
        cwd = Path.cwd()
        if cwd.name == "scripts":
            return cwd.parent
        return cwd

    def get_dataroom_path(self) -> Path:
        """Get absolute path to dataroom directory."""
        return self.get_project_root() / self.dataroom_dir

    def get_working_path(self) -> Path:
        """Get absolute path to working directory."""
        return self.get_project_root() / self.working_dir

    def get_output_path(self) -> Path:
        """Get absolute path to output directory."""
        return self.get_project_root() / self.output_dir


# Default configuration instance
DEFAULT_CONFIG = Config()
