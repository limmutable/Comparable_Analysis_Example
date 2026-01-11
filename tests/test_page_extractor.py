"""Tests for page extractor module."""

import pytest
from pathlib import Path
import tempfile
import os

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from lib.config import Config
from lib.page_extractor import PageExtractor, ExtractionResult


class TestExtractionResult:
    """Tests for ExtractionResult dataclass."""

    def test_page_range_property(self):
        """Test page range formatting."""
        result = ExtractionResult(
            success=True,
            source_path=Path("test.pdf"),
            start_page=10,
            end_page=20
        )
        assert result.page_range == "10-20"

    def test_to_dict(self):
        """Test dictionary serialization."""
        result = ExtractionResult(
            success=True,
            source_path=Path("/test/file.pdf"),
            output_path=Path("/output/file.txt"),
            pages_extracted=10,
            start_page=1,
            end_page=10,
            text_size=5000,
            estimated_tokens=1250
        )
        d = result.to_dict()
        assert d["success"] is True
        assert d["source_path"] == "/test/file.pdf"
        assert d["page_range"] == "1-10"
        assert d["text_size"] == 5000


class TestPageExtractor:
    """Tests for PageExtractor class."""

    @pytest.fixture
    def extractor(self):
        """Create a PageExtractor instance."""
        return PageExtractor()

    @pytest.fixture
    def temp_output_dir(self):
        """Create a temporary output directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def test_generate_output_path(self, extractor):
        """Test output path generation."""
        source = Path("/dataroom/nota/nota-sec.pdf")
        output = extractor.generate_output_path(source, 80, 120, company="nota")

        assert output.name == "nota-sec-80-120.txt"
        assert "nota" in str(output)

    def test_generate_output_path_auto_company(self, extractor):
        """Test output path generation with auto-detected company."""
        source = Path("/dataroom/acme/filing.pdf")
        output = extractor.generate_output_path(source, 1, 10)

        assert output.name == "filing-1-10.txt"
        assert "acme" in str(output)

    def test_extract_nonexistent_file(self, extractor):
        """Test extraction from non-existent file."""
        result = extractor.extract_pages(
            Path("/nonexistent/file.pdf"),
            1, 10
        )
        assert result.success is False
        assert "not found" in result.error_message.lower()

    def test_extraction_result_failure(self):
        """Test failed extraction result."""
        result = ExtractionResult(
            success=False,
            source_path=Path("test.pdf"),
            error_message="Test error"
        )
        assert result.success is False
        assert result.error_message == "Test error"


class TestPageExtractorWithRealPDF:
    """Tests that require a real PDF file.

    These tests are skipped if no test PDF is available.
    """

    @pytest.fixture
    def test_pdf_path(self):
        """Get path to test PDF if available."""
        # Look for the nota PDF in the project
        project_root = Path(__file__).parent.parent
        pdf_path = project_root / "dataroom" / "nota" / "nota-sec.pdf"

        if pdf_path.exists():
            return pdf_path
        pytest.skip("Test PDF not available")

    @pytest.fixture
    def extractor_with_temp_config(self):
        """Create extractor with temporary working directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = Config()
            # Override working directory
            config.working_dir = tmpdir
            extractor = PageExtractor(config)
            yield extractor, Path(tmpdir)

    def test_get_page_count(self, test_pdf_path):
        """Test getting page count from real PDF."""
        extractor = PageExtractor()
        count = extractor.get_page_count(test_pdf_path)
        assert count > 0
        # nota-sec.pdf should have many pages
        assert count > 100

    def test_extract_pages_real_pdf(self, test_pdf_path, extractor_with_temp_config):
        """Test extracting pages from real PDF."""
        extractor, temp_dir = extractor_with_temp_config

        result = extractor.extract_pages(
            test_pdf_path,
            start_page=1,
            end_page=3,
            output_path=temp_dir / "test-output.txt"
        )

        assert result.success is True
        assert result.pages_extracted == 3
        assert result.output_path.exists()
        assert result.text_size > 0

        # Verify content was written
        content = result.output_path.read_text()
        assert "Page 1" in content
        assert "Page 2" in content
        assert "Page 3" in content

    def test_extract_invalid_page_range(self, test_pdf_path):
        """Test extraction with invalid page range."""
        extractor = PageExtractor()

        # Start > End should fail
        result = extractor.extract_pages(
            test_pdf_path,
            start_page=100,
            end_page=50
        )

        assert result.success is False
        assert "invalid" in result.error_message.lower()

    def test_extract_adjusts_page_range(self, test_pdf_path, extractor_with_temp_config):
        """Test that page range is adjusted to actual pages."""
        extractor, temp_dir = extractor_with_temp_config
        total_pages = extractor.get_page_count(test_pdf_path)

        # Request more pages than exist
        result = extractor.extract_pages(
            test_pdf_path,
            start_page=total_pages - 2,
            end_page=total_pages + 100,  # Beyond actual pages
            output_path=temp_dir / "test-output.txt"
        )

        assert result.success is True
        # Should only extract actual pages
        assert result.end_page == total_pages
