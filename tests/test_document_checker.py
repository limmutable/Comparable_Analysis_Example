"""Tests for document checker module."""

import pytest
from pathlib import Path
import tempfile
import os

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from lib.config import Config
from lib.document_checker import DocumentChecker, FileInfo, FileStatus


class TestFileInfo:
    """Tests for FileInfo dataclass."""

    def test_size_conversions(self):
        """Test size conversion properties."""
        info = FileInfo(
            path=Path("test.pdf"),
            exists=True,
            size_bytes=1024 * 1024,  # 1 MB
            estimated_tokens=200_000,
            status=FileStatus.OK
        )
        assert info.size_mb == 1.0
        assert info.size_kb == 1024.0
        assert info.tokens_k == 200.0

    def test_status_properties(self):
        """Test status check properties."""
        ok_info = FileInfo(Path("test.pdf"), True, status=FileStatus.OK)
        assert ok_info.is_ok is True
        assert ok_info.is_too_large is False

        large_info = FileInfo(Path("test.pdf"), True, status=FileStatus.TOO_LARGE)
        assert large_info.is_ok is False
        assert large_info.is_too_large is True

    def test_to_dict(self):
        """Test dictionary serialization."""
        info = FileInfo(
            path=Path("/test/file.pdf"),
            exists=True,
            size_bytes=1000,
            estimated_tokens=222,
            status=FileStatus.OK
        )
        d = info.to_dict()
        assert d["path"] == "/test/file.pdf"
        assert d["exists"] is True
        assert d["size_bytes"] == 1000
        assert d["status"] == "ok"


class TestDocumentChecker:
    """Tests for DocumentChecker class."""

    @pytest.fixture
    def checker(self):
        """Create a DocumentChecker instance."""
        return DocumentChecker()

    @pytest.fixture
    def temp_file(self):
        """Create a temporary file for testing."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
            f.write(b"x" * 1000)  # 1KB file
            path = Path(f.name)
        yield path
        os.unlink(path)

    def test_estimate_tokens_text(self, checker, temp_file):
        """Test token estimation for text files."""
        tokens = checker.estimate_tokens(temp_file)
        # 1000 bytes / 4.0 bytes per token = 250 tokens
        assert tokens == 250

    def test_estimate_tokens_nonexistent(self, checker):
        """Test token estimation for non-existent file."""
        tokens = checker.estimate_tokens(Path("/nonexistent/file.pdf"))
        assert tokens == 0

    def test_get_status_ok(self, checker):
        """Test status for small files."""
        status = checker.get_status(100_000)
        assert status == FileStatus.OK

    def test_get_status_warning(self, checker):
        """Test status for medium files."""
        status = checker.get_status(300_000)
        assert status == FileStatus.WARNING

    def test_get_status_too_large(self, checker):
        """Test status for large files."""
        status = checker.get_status(600_000)
        assert status == FileStatus.TOO_LARGE

    def test_check_file_exists(self, checker, temp_file):
        """Test checking an existing file."""
        info = checker.check_file(temp_file)
        assert info.exists is True
        assert info.size_bytes == 1000
        assert info.status == FileStatus.OK

    def test_check_file_not_found(self, checker):
        """Test checking a non-existent file."""
        info = checker.check_file(Path("/nonexistent/file.pdf"))
        assert info.exists is False
        assert info.status == FileStatus.NOT_FOUND
        assert "not found" in info.error_message.lower()

    def test_check_directory(self, checker):
        """Test checking a directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create some test files
            for i in range(3):
                path = Path(tmpdir) / f"file{i}.txt"
                path.write_text("test content")

            infos = checker.check_directory(Path(tmpdir), "*.txt")
            assert len(infos) == 3
            assert all(info.exists for info in infos)

    def test_check_empty_directory(self, checker):
        """Test checking an empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            infos = checker.check_directory(Path(tmpdir), "*.pdf")
            assert len(infos) == 0


class TestDocumentCheckerWithCustomConfig:
    """Tests for DocumentChecker with custom configuration."""

    def test_custom_token_limit(self):
        """Test with custom token limits."""
        config = Config(
            safe_token_limit=100_000,
            warning_token_limit=50_000
        )
        checker = DocumentChecker(config)

        assert checker.get_status(40_000) == FileStatus.OK
        assert checker.get_status(60_000) == FileStatus.WARNING
        assert checker.get_status(150_000) == FileStatus.TOO_LARGE

    def test_custom_bytes_per_token(self):
        """Test with custom bytes per token ratio."""
        config = Config(bytes_per_token_text=2.0)
        checker = DocumentChecker(config)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
            f.write(b"x" * 1000)
            path = Path(f.name)

        try:
            tokens = checker.estimate_tokens(path)
            # 1000 bytes / 2.0 bytes per token = 500 tokens
            assert tokens == 500
        finally:
            os.unlink(path)
