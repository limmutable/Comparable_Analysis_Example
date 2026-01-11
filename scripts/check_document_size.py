#!/usr/bin/env python3
"""
Document Size Checker

Checks document sizes and estimates token counts to help avoid
context window limits when using LLM tools.

Usage:
    python scripts/check_document_size.py dataroom/
    python scripts/check_document_size.py dataroom/nota/nota-sec.pdf
    python scripts/check_document_size.py dataroom/ --limit 500000
"""

import os
import sys
import argparse
from pathlib import Path

# Rough token estimation factors
# These are approximations - actual tokens vary by content
BYTES_PER_TOKEN_PDF = 4.5  # PDFs have formatting overhead
BYTES_PER_TOKEN_TEXT = 4.0  # Plain text
BYTES_PER_TOKEN_XLSX = 3.0  # Excel files (lots of numbers)

# Context window limits (approximate, leave buffer)
CONTEXT_LIMITS = {
    "claude-3.5-sonnet": 200_000,
    "claude-3-opus": 200_000,
    "gemini-1.5-pro": 1_000_000,
    "gemini-1.5-flash": 1_000_000,
    "gpt-4-turbo": 128_000,
    "gpt-4o": 128_000,
}

# Safe limits (leave 30% buffer for prompts and responses)
SAFE_TOKEN_LIMIT = 500_000  # Conservative default


def estimate_tokens(file_path: Path) -> int:
    """Estimate token count for a file."""
    size_bytes = file_path.stat().st_size
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return int(size_bytes / BYTES_PER_TOKEN_PDF)
    elif suffix in [".xlsx", ".xls", ".csv"]:
        return int(size_bytes / BYTES_PER_TOKEN_XLSX)
    else:
        return int(size_bytes / BYTES_PER_TOKEN_TEXT)


def format_size(size_bytes: int) -> str:
    """Format bytes as human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def format_tokens(tokens: int) -> str:
    """Format token count with K/M suffix."""
    if tokens < 1000:
        return str(tokens)
    elif tokens < 1_000_000:
        return f"{tokens/1000:.1f}K"
    else:
        return f"{tokens/1_000_000:.2f}M"


def check_file(file_path: Path, limit: int) -> dict:
    """Check a single file and return info."""
    if not file_path.exists():
        return {"error": f"File not found: {file_path}"}

    size_bytes = file_path.stat().st_size
    estimated_tokens = estimate_tokens(file_path)

    return {
        "path": str(file_path),
        "name": file_path.name,
        "size_bytes": size_bytes,
        "size_human": format_size(size_bytes),
        "estimated_tokens": estimated_tokens,
        "tokens_human": format_tokens(estimated_tokens),
        "exceeds_limit": estimated_tokens > limit,
        "pct_of_limit": (estimated_tokens / limit) * 100,
    }


def check_directory(dir_path: Path, limit: int) -> list:
    """Check all supported files in a directory."""
    supported_extensions = {".pdf", ".txt", ".md", ".csv", ".xlsx", ".xls", ".json"}
    results = []

    for file_path in sorted(dir_path.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            results.append(check_file(file_path, limit))

    return results


def print_results(results: list, limit: int):
    """Print results in a formatted table."""
    if not results:
        print("No supported files found.")
        return

    # Header
    print("\n" + "=" * 80)
    print(f"{'File':<40} {'Size':<10} {'Est. Tokens':<12} {'% Limit':<10} {'Status'}")
    print("=" * 80)

    total_tokens = 0
    exceeds_count = 0

    for r in results:
        if "error" in r:
            print(f"ERROR: {r['error']}")
            continue

        status = "⚠️  TOO LARGE" if r["exceeds_limit"] else "✓ OK"
        if r["exceeds_limit"]:
            exceeds_count += 1

        # Truncate long file names
        name = r["name"]
        if len(name) > 38:
            name = name[:35] + "..."

        print(f"{name:<40} {r['size_human']:<10} {r['tokens_human']:<12} {r['pct_of_limit']:>6.1f}%    {status}")
        total_tokens += r["estimated_tokens"]

    # Summary
    print("=" * 80)
    print(f"{'TOTAL':<40} {'':<10} {format_tokens(total_tokens):<12} {(total_tokens/limit)*100:>6.1f}%")
    print(f"\nToken Limit: {format_tokens(limit)} (configurable with --limit)")

    if exceeds_count > 0:
        print(f"\n⚠️  {exceeds_count} file(s) exceed the token limit.")
        print("\nRecommended actions:")
        print("  1. Extract specific pages/sections from large PDFs")
        print("  2. Use page range extraction: 'Read pages 45-60 of the 10-K'")
        print("  3. Split analysis into multiple smaller requests")
        print("  4. Use the extract_sections.py script to pre-extract key sections")
    elif total_tokens > limit:
        print(f"\n⚠️  Combined files exceed limit. Analyze files separately.")
    else:
        print(f"\n✓ All files within token limit.")


def main():
    parser = argparse.ArgumentParser(
        description="Check document sizes and estimate token counts"
    )
    parser.add_argument(
        "path",
        type=str,
        help="File or directory to check"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=SAFE_TOKEN_LIMIT,
        help=f"Token limit to check against (default: {SAFE_TOKEN_LIMIT})"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()
    path = Path(args.path)

    if not path.exists():
        print(f"Error: Path not found: {path}")
        sys.exit(1)

    if path.is_file():
        results = [check_file(path, args.limit)]
    else:
        results = check_directory(path, args.limit)

    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        print_results(results, args.limit)


if __name__ == "__main__":
    main()
