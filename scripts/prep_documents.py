#!/usr/bin/env python3
"""
Document preparation CLI for financial analysis.

Prepares large PDF documents for analysis by extracting key sections
to smaller text files that fit within LLM context windows.

Usage:
    # Check a company's documents
    python prep_documents.py check nota

    # Prepare documents (extract if needed)
    python prep_documents.py prep nota

    # Extract specific pages
    python prep_documents.py extract nota --pages 150-200

    # Force re-extraction
    python prep_documents.py prep nota --force

    # Show status of all companies
    python prep_documents.py status
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from lib import PrepWorkflow, Config


def cmd_check(args, workflow: PrepWorkflow) -> int:
    """Check a company's documents."""
    result = workflow.check_company(args.company)
    print(result.format_report())
    return 0 if result.success else 1


def cmd_prep(args, workflow: PrepWorkflow) -> int:
    """Prepare a company's documents for analysis."""
    result = workflow.prepare_company(
        args.company,
        force=args.force,
        filing_type=args.filing_type
    )

    print(result.format_report())

    if args.json:
        print("\n---\n")
        print(json.dumps(result.to_dict(), indent=2))

    return 0 if result.success else 1


def cmd_extract(args, workflow: PrepWorkflow) -> int:
    """Extract specific pages from a PDF."""
    # Parse page range
    if "-" in args.pages:
        start, end = args.pages.split("-")
        start_page = int(start)
        end_page = int(end)
    else:
        start_page = int(args.pages)
        end_page = start_page

    result = workflow.extract_pages(
        args.company,
        start_page,
        end_page,
        source_file=args.file
    )

    if result.success:
        print(f"✓ Extracted pages {result.page_range}")
        print(f"  Output: {result.output_path}")
        print(f"  Size: {result.text_size:,} chars (~{result.estimated_tokens:,} tokens)")
    else:
        print(f"✗ Extraction failed: {result.error_message}")

    return 0 if result.success else 1


def cmd_status(args, workflow: PrepWorkflow) -> int:
    """Show status of all companies in dataroom."""
    dataroom = workflow.config.get_dataroom_path()

    if not dataroom.exists():
        print(f"Dataroom not found: {dataroom}")
        return 1

    companies = [d.name for d in dataroom.iterdir() if d.is_dir()]

    if not companies:
        print("No companies found in dataroom/")
        return 0

    print("## Company Status\n")
    print("| Company | Source Files | Working Files | Status |")
    print("|---------|--------------|---------------|--------|")

    for company in sorted(companies):
        result = workflow.check_company(company)
        source_count = len(result.source_files)
        working_count = len(result.working_files)

        if result.needs_extraction:
            status = "⚠️ Needs extraction"
        elif working_count > 0:
            status = "✓ Ready"
        elif source_count > 0:
            # Check if files are small enough
            all_ok = all(f.is_ok for f in result.source_files)
            status = "✓ Small files" if all_ok else "⚠️ Check needed"
        else:
            status = "- Empty"

        print(f"| {company} | {source_count} | {working_count} | {status} |")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Prepare documents for financial analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s check nota           Check nota's documents
  %(prog)s prep nota            Prepare nota for analysis
  %(prog)s prep nota --force    Force re-extraction
  %(prog)s extract nota --pages 150-200
  %(prog)s status               Show all companies
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Check command
    check_parser = subparsers.add_parser("check", help="Check a company's documents")
    check_parser.add_argument("company", help="Company name/directory")

    # Prep command
    prep_parser = subparsers.add_parser("prep", help="Prepare documents for analysis")
    prep_parser.add_argument("company", help="Company name/directory")
    prep_parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Force re-extraction even if working files exist"
    )
    prep_parser.add_argument(
        "--filing-type", "-t",
        choices=["auto", "10k", "korean_sec"],
        default="auto",
        help="Type of filing (default: auto-detect)"
    )
    prep_parser.add_argument(
        "--json",
        action="store_true",
        help="Also output JSON result"
    )

    # Extract command
    extract_parser = subparsers.add_parser("extract", help="Extract specific pages")
    extract_parser.add_argument("company", help="Company name/directory")
    extract_parser.add_argument(
        "--pages", "-p",
        required=True,
        help="Page range (e.g., 150-200 or 150)"
    )
    extract_parser.add_argument(
        "--file", "-f",
        help="Specific PDF filename (uses first PDF if not specified)"
    )

    # Status command
    subparsers.add_parser("status", help="Show status of all companies")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Initialize workflow
    config = Config()
    workflow = PrepWorkflow(config)

    # Dispatch command
    commands = {
        "check": cmd_check,
        "prep": cmd_prep,
        "extract": cmd_extract,
        "status": cmd_status,
    }

    return commands[args.command](args, workflow)


if __name__ == "__main__":
    sys.exit(main())
