"""Tests for configuration module."""

import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from lib.config import Config, DEFAULT_CONFIG


class TestConfig:
    """Tests for Config class."""

    def test_default_values(self):
        """Test default configuration values."""
        config = Config()
        assert config.bytes_per_token_pdf == 4.5
        assert config.bytes_per_token_text == 4.0
        assert config.safe_token_limit == 500_000
        assert config.warning_token_limit == 200_000

    def test_default_page_ranges(self):
        """Test default page ranges for 10-K."""
        config = Config()
        ranges = config.default_page_ranges
        assert len(ranges) > 0
        assert (1, 30) in ranges
        assert (80, 130) in ranges

    def test_korean_sec_page_ranges(self):
        """Test Korean SEC filing page ranges."""
        config = Config()
        ranges = config.korean_sec_page_ranges
        assert len(ranges) > 0
        # Korean filings have different page ranges
        assert (150, 200) in ranges

    def test_custom_values(self):
        """Test custom configuration values."""
        config = Config(
            bytes_per_token_pdf=5.0,
            safe_token_limit=1_000_000
        )
        assert config.bytes_per_token_pdf == 5.0
        assert config.safe_token_limit == 1_000_000

    def test_directory_paths(self):
        """Test directory path configuration."""
        config = Config()
        assert config.dataroom_dir == "dataroom"
        assert config.working_dir == ".working"
        assert config.output_dir == "output"

    def test_default_config_singleton(self):
        """Test DEFAULT_CONFIG is properly configured."""
        assert DEFAULT_CONFIG.bytes_per_token_pdf == 4.5
        assert DEFAULT_CONFIG.safe_token_limit == 500_000
