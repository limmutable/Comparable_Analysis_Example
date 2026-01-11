"""Tests for workflow module."""

import pytest
from pathlib import Path
import tempfile
import os

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from lib.config import Config
from lib.workflow import PrepWorkflow, WorkflowResult
from lib.document_checker import FileStatus


class TestWorkflowResult:
    """Tests for WorkflowResult dataclass."""

    def test_total_working_tokens(self):
        """Test total token calculation."""
        from lib.document_checker import FileInfo

        result = WorkflowResult(
            company="test",
            success=True,
            working_files=[
                FileInfo(Path("a.txt"), True, estimated_tokens=1000, status=FileStatus.OK),
                FileInfo(Path("b.txt"), True, estimated_tokens=2000, status=FileStatus.OK),
            ]
        )
        assert result.total_working_tokens == 3000

    def test_files_ready(self):
        """Test files ready list."""
        from lib.document_checker import FileInfo

        result = WorkflowResult(
            company="test",
            success=True,
            working_files=[
                FileInfo(Path("/a.txt"), True, status=FileStatus.OK),
                FileInfo(Path("/b.txt"), True, status=FileStatus.WARNING),
                FileInfo(Path("/c.txt"), True, status=FileStatus.OK),
            ]
        )
        assert len(result.files_ready) == 2

    def test_format_report(self):
        """Test report formatting."""
        result = WorkflowResult(
            company="acme",
            success=True
        )
        report = result.format_report()
        assert "acme" in report
        assert "Document Preparation" in report

    def test_to_dict(self):
        """Test dictionary serialization."""
        result = WorkflowResult(
            company="test",
            success=True,
            needs_extraction=True
        )
        d = result.to_dict()
        assert d["company"] == "test"
        assert d["success"] is True
        assert d["needs_extraction"] is True


class TestPrepWorkflow:
    """Tests for PrepWorkflow class."""

    @pytest.fixture
    def workflow_with_temp_dirs(self):
        """Create workflow with temporary directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create directory structure
            dataroom = tmppath / "dataroom"
            working = tmppath / ".working"
            dataroom.mkdir()
            working.mkdir()

            # Create config pointing to temp dirs
            config = Config(
                dataroom_dir=str(dataroom),
                working_dir=str(working)
            )
            # Override get methods to return absolute paths
            config._project_root = tmppath

            workflow = PrepWorkflow(config)
            # Patch the config methods
            workflow.config.get_project_root = lambda: tmppath
            workflow.config.get_dataroom_path = lambda: dataroom
            workflow.config.get_working_path = lambda: working

            yield workflow, dataroom, working

    def test_check_empty_company(self, workflow_with_temp_dirs):
        """Test checking a company with no files."""
        workflow, dataroom, working = workflow_with_temp_dirs

        # Create empty company directory
        (dataroom / "empty_co").mkdir()

        result = workflow.check_company("empty_co")
        assert result.success is True
        assert len(result.source_files) == 0
        assert len(result.working_files) == 0

    def test_check_company_with_working_files(self, workflow_with_temp_dirs):
        """Test checking a company with existing working files."""
        workflow, dataroom, working = workflow_with_temp_dirs

        # Create company directories
        (dataroom / "acme").mkdir()
        (working / "acme").mkdir()

        # Create a working file
        (working / "acme" / "extract.txt").write_text("test content")

        result = workflow.check_company("acme")
        assert result.success is True
        assert len(result.working_files) == 1
        assert result.needs_extraction is False


class TestPrepWorkflowWithRealFiles:
    """Tests that use real project files.

    These tests are skipped if required files don't exist.
    """

    @pytest.fixture
    def project_workflow(self):
        """Get workflow for the real project."""
        project_root = Path(__file__).parent.parent
        pdf_path = project_root / "dataroom" / "nota" / "nota-sec.pdf"

        if not pdf_path.exists():
            pytest.skip("Project PDF not available")

        return PrepWorkflow()

    def test_check_nota(self, project_workflow):
        """Test checking the nota company."""
        result = project_workflow.check_company("nota")

        assert result.success is True
        assert result.company == "nota"
        assert len(result.source_files) > 0

        # Source file should be too large
        assert any(f.is_too_large for f in result.source_files)

    def test_check_finds_working_files(self, project_workflow):
        """Test that existing working files are found."""
        result = project_workflow.check_company("nota")

        # Should find existing .working/nota/ files
        if result.working_files:
            assert all(f.exists for f in result.working_files)
            assert all(".working" in str(f.path) for f in result.working_files)

    def test_extract_specific_pages(self, project_workflow):
        """Test extracting specific pages."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = project_workflow.extract_pages(
                "nota",
                start_page=1,
                end_page=5
            )

            assert result.success is True
            assert result.pages_extracted == 5
            assert result.output_path.exists()
