#!/usr/bin/env python3
"""
SEC Filing Section Extractor

Helps identify and extract specific sections from SEC filings
to work within LLM context window limits.

For 10-K filings, the key financial data is typically in:
- Item 6: Selected Financial Data (pages ~30-35)
- Item 7: MD&A (pages ~35-70)
- Item 8: Financial Statements (pages ~70-120)

Usage:
    python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --info
    python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 70-120 --output output/nota/financials.txt

Note: For full PDF extraction, install PyPDF2:
    pip install PyPDF2
"""

import os
import sys
import argparse
from pathlib import Path

# Try to import PyPDF2, but don't fail if not installed
try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False


# Common 10-K section page ranges (approximate)
SEC_10K_SECTIONS = {
    "cover": {"pages": "1-5", "description": "Cover page, table of contents"},
    "business": {"pages": "6-25", "description": "Item 1: Business description"},
    "risk_factors": {"pages": "25-45", "description": "Item 1A: Risk factors"},
    "selected_financial": {"pages": "45-50", "description": "Item 6: Selected financial data (5-year summary)"},
    "mda": {"pages": "50-80", "description": "Item 7: Management Discussion & Analysis"},
    "financials": {"pages": "80-130", "description": "Item 8: Financial statements and notes"},
    "controls": {"pages": "130-140", "description": "Item 9A: Controls and procedures"},
    "exhibits": {"pages": "140+", "description": "Item 15: Exhibits"},
}

# Key sections for financial analysis
ANALYSIS_SECTIONS = ["selected_financial", "mda", "financials"]


def get_pdf_info(pdf_path: Path) -> dict:
    """Get basic PDF information."""
    if not HAS_PYPDF2:
        # Estimate based on file size
        size_bytes = pdf_path.stat().st_size
        estimated_pages = size_bytes // 50000  # Rough estimate: 50KB per page
        return {
            "path": str(pdf_path),
            "size_mb": size_bytes / (1024 * 1024),
            "estimated_pages": estimated_pages,
            "note": "Install PyPDF2 for accurate page count: pip install PyPDF2"
        }

    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return {
            "path": str(pdf_path),
            "size_mb": pdf_path.stat().st_size / (1024 * 1024),
            "pages": len(reader.pages),
            "metadata": dict(reader.metadata) if reader.metadata else {}
        }


def extract_pages(pdf_path: Path, start_page: int, end_page: int, output_path: Path = None) -> str:
    """Extract text from specific pages of a PDF."""
    if not HAS_PYPDF2:
        print("Error: PyPDF2 required for extraction. Install with: pip install PyPDF2")
        print("\nAlternative: Use Claude's page-range reading:")
        print(f'  > "Read pages {start_page}-{end_page} of {pdf_path}"')
        sys.exit(1)

    text_content = []

    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        total_pages = len(reader.pages)

        # Adjust for 0-based indexing
        start_idx = max(0, start_page - 1)
        end_idx = min(total_pages, end_page)

        print(f"Extracting pages {start_page}-{end_page} of {total_pages}...")

        for i in range(start_idx, end_idx):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                text_content.append(f"\n--- Page {i+1} ---\n")
                text_content.append(text)

    full_text = "\n".join(text_content)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Saved to: {output_path}")
        print(f"Extracted text size: {len(full_text):,} characters (~{len(full_text)//4:,} tokens)")

    return full_text


def print_section_guide():
    """Print guide for 10-K sections."""
    print("\n" + "=" * 70)
    print("10-K SECTION GUIDE")
    print("=" * 70)
    print("\nTypical 10-K sections and page ranges:\n")

    for section, info in SEC_10K_SECTIONS.items():
        marker = "★" if section in ANALYSIS_SECTIONS else " "
        print(f"  {marker} {section:<20} Pages {info['pages']:<10} {info['description']}")

    print("\n★ = Key sections for financial analysis")
    print("\n" + "-" * 70)
    print("RECOMMENDED EXTRACTION STRATEGY")
    print("-" * 70)
    print("""
For comparable analysis, extract these sections in order:

1. QUICK SCAN (low tokens):
   > "Read pages 1-5 of the 10-K and summarize the company"

2. FINANCIAL SUMMARY (medium tokens):
   > "Read pages 45-50 (Item 6: Selected Financial Data)"

3. FULL FINANCIALS (high tokens - may need chunking):
   > "Read pages 80-100 (Income Statement, Balance Sheet)"
   > "Read pages 100-120 (Cash Flow, Notes to Financials)"

4. MD&A for context (medium-high tokens):
   > "Read pages 50-70 (Item 7: MD&A highlights)"
""")


def print_chunking_strategies():
    """Print strategies for handling large documents."""
    print("\n" + "=" * 70)
    print("CHUNKING STRATEGIES FOR LARGE DOCUMENTS")
    print("=" * 70)
    print("""
When a document exceeds the context window, use these strategies:

STRATEGY 1: Page Range Reading
------------------------------
Instead of reading the entire file, specify page ranges:

  > "Read pages 80-100 of dataroom/nota/nota-sec.pdf and extract
     the Income Statement and Balance Sheet"

  > "Read pages 100-120 of the same file and extract the
     Cash Flow Statement and key notes"


STRATEGY 2: Section-by-Section Analysis
---------------------------------------
Break the analysis into multiple requests:

  Request 1: "Read the 10-K cover and Item 1 (pages 1-25).
              Summarize the business model."

  Request 2: "Read Item 6 Selected Financial Data (pages 45-50).
              Extract the 5-year financial summary."

  Request 3: "Read the Financial Statements (pages 80-120).
              Extract Income Statement, Balance Sheet, Cash Flow."


STRATEGY 3: Pre-extraction with Scripts
---------------------------------------
Use this script to extract text from specific pages:

  python scripts/extract_sections.py dataroom/nota/nota-sec.pdf \\
      --pages 80-120 --output output/nota/financials.txt

Then analyze the smaller extracted file:
  > "Read output/nota/financials.txt and extract key metrics"


STRATEGY 4: Targeted Queries
----------------------------
Ask for specific data points rather than full analysis:

  > "In the 10-K at dataroom/nota/nota-sec.pdf, find and extract:
     - Total Revenue for FY2023 and FY2022
     - Net Income for FY2023 and FY2022
     - Total Assets and Total Liabilities as of year-end
     Search in Item 6 or Item 8 (Financial Statements)"


STRATEGY 5: Use Smaller Source Files
------------------------------------
For recurring analysis, consider:
  - Download earnings releases (usually <20 pages)
  - Use investor presentations (more concise)
  - Extract key tables to CSV manually
""")


def main():
    parser = argparse.ArgumentParser(
        description="Extract sections from SEC filings"
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        help="PDF file to analyze/extract"
    )
    parser.add_argument(
        "--info", "-i",
        action="store_true",
        help="Show PDF info and page count"
    )
    parser.add_argument(
        "--guide", "-g",
        action="store_true",
        help="Show 10-K section guide"
    )
    parser.add_argument(
        "--strategies", "-s",
        action="store_true",
        help="Show chunking strategies for large documents"
    )
    parser.add_argument(
        "--pages", "-p",
        type=str,
        help="Page range to extract (e.g., '80-120')"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path for extracted text"
    )

    args = parser.parse_args()

    # Show guides if requested
    if args.guide:
        print_section_guide()
        return

    if args.strategies:
        print_chunking_strategies()
        return

    # If no path and no flags, show help
    if not args.path and not args.guide and not args.strategies:
        print("Document Size & Extraction Helper")
        print("=" * 40)
        print("\nUsage examples:")
        print("  python scripts/extract_sections.py --guide")
        print("  python scripts/extract_sections.py --strategies")
        print("  python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --info")
        print("  python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 80-120")
        return

    path = Path(args.path)

    if not path.exists():
        print(f"Error: File not found: {path}")
        sys.exit(1)

    # Show info
    if args.info or not args.pages:
        info = get_pdf_info(path)
        print("\nPDF Information:")
        print("-" * 40)
        for key, value in info.items():
            if key == "size_mb":
                print(f"  {key}: {value:.2f} MB")
            else:
                print(f"  {key}: {value}")

        if not args.pages:
            print("\nTo extract specific pages, use:")
            print(f"  python scripts/extract_sections.py {path} --pages 80-120")
            print("\nFor section guide, use:")
            print("  python scripts/extract_sections.py --guide")
        return

    # Extract pages
    if args.pages:
        try:
            start, end = map(int, args.pages.split("-"))
        except ValueError:
            print(f"Error: Invalid page range '{args.pages}'. Use format: START-END (e.g., 80-120)")
            sys.exit(1)

        output_path = Path(args.output) if args.output else None
        extract_pages(path, start, end, output_path)


if __name__ == "__main__":
    main()
