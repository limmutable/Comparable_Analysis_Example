"""
Document preparation library for financial analysis.

Modules:
- config: Configuration constants and defaults
- document_checker: Check file sizes and token estimates
- page_extractor: Extract pages from PDFs
- workflow: High-level workflow orchestration
"""

from .config import Config
from .document_checker import DocumentChecker, FileInfo
from .page_extractor import PageExtractor, ExtractionResult
from .workflow import PrepWorkflow, WorkflowResult

__all__ = [
    "Config",
    "DocumentChecker",
    "FileInfo",
    "PageExtractor",
    "ExtractionResult",
    "PrepWorkflow",
    "WorkflowResult",
]
