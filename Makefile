# Comparable Analysis Project Makefile
# Uses uv for Python package management
#
# Usage:
#   make setup     - Install uv and project dependencies
#   make check     - Check document sizes in dataroom
#   make extract   - Extract PDF sections (interactive)
#   make clean     - Clean generated files

.PHONY: setup setup-uv install check extract clean clean-working clean-all help test lint

# Default target
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[34m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
RESET := \033[0m

#---------------------------------------------------------------------------
# Setup & Installation
#---------------------------------------------------------------------------

## Install uv package manager (if not installed)
setup-uv:
	@echo "$(BLUE)Checking for uv...$(RESET)"
	@if ! command -v uv &> /dev/null; then \
		echo "$(YELLOW)Installing uv...$(RESET)"; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		echo "$(GREEN)uv installed. Please restart your terminal or run: source ~/.bashrc$(RESET)"; \
	else \
		echo "$(GREEN)uv is already installed: $$(uv --version)$(RESET)"; \
	fi

## Full project setup: install uv, create venv, install dependencies
setup: setup-uv
	@echo "$(BLUE)Setting up project...$(RESET)"
	@echo "$(BLUE)Creating virtual environment and installing dependencies...$(RESET)"
	uv venv
	uv pip install -e .
	@echo ""
	@echo "$(GREEN)========================================$(RESET)"
	@echo "$(GREEN)Setup complete!$(RESET)"
	@echo "$(GREEN)========================================$(RESET)"
	@echo ""
	@echo "To activate the virtual environment:"
	@echo "  source .venv/bin/activate"
	@echo ""
	@echo "Or use 'make' commands which use 'uv run' automatically:"
	@echo "  make check    - Check document sizes"
	@echo "  make extract  - Extract PDF sections"
	@echo ""

## Install dependencies only (assumes uv is installed)
install:
	@echo "$(BLUE)Installing dependencies...$(RESET)"
	uv pip install -e .
	@echo "$(GREEN)Dependencies installed.$(RESET)"

## Install dev dependencies
install-dev:
	@echo "$(BLUE)Installing dev dependencies...$(RESET)"
	uv pip install -e ".[dev]"
	@echo "$(GREEN)Dev dependencies installed.$(RESET)"

#---------------------------------------------------------------------------
# Document Processing
#---------------------------------------------------------------------------

## Check document sizes in dataroom (detect files that exceed context limits)
check:
	@echo "$(BLUE)Checking document sizes...$(RESET)"
	@uv run python scripts/check_document_size.py dataroom/

## Check a specific file: make check-file FILE=dataroom/nota/nota-sec.pdf
check-file:
	@if [ -z "$(FILE)" ]; then \
		echo "$(RED)Error: FILE not specified$(RESET)"; \
		echo "Usage: make check-file FILE=dataroom/nota/nota-sec.pdf"; \
		exit 1; \
	fi
	@uv run python scripts/check_document_size.py $(FILE)

## Show 10-K section guide
guide:
	@uv run python scripts/extract_sections.py --guide

## Show chunking strategies for large documents
strategies:
	@uv run python scripts/extract_sections.py --strategies

## Get PDF info: make pdf-info FILE=dataroom/nota/nota-sec.pdf
pdf-info:
	@if [ -z "$(FILE)" ]; then \
		echo "$(RED)Error: FILE not specified$(RESET)"; \
		echo "Usage: make pdf-info FILE=dataroom/nota/nota-sec.pdf"; \
		exit 1; \
	fi
	@uv run python scripts/extract_sections.py $(FILE) --info

## Extract pages from PDF: make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120 [OUT=.working/nota/financials.txt]
## OUT defaults to .working/{company}/{filename}-{pages}.txt if not specified
extract-pages:
	@if [ -z "$(FILE)" ] || [ -z "$(PAGES)" ]; then \
		echo "$(RED)Error: FILE and PAGES required$(RESET)"; \
		echo "Usage: make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120"; \
		echo "       make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120 OUT=.working/nota/financials.txt"; \
		exit 1; \
	fi
	@if [ -z "$(OUT)" ]; then \
		COMPANY=$$(basename $$(dirname $(FILE))); \
		FILENAME=$$(basename $(FILE) .pdf); \
		OUT_PATH=".working/$${COMPANY}/$${FILENAME}-$(PAGES).txt"; \
		mkdir -p ".working/$${COMPANY}"; \
		echo "$(BLUE)Extracting to: $${OUT_PATH}$(RESET)"; \
		uv run python scripts/extract_sections.py $(FILE) --pages $(PAGES) --output "$${OUT_PATH}"; \
	else \
		mkdir -p $$(dirname $(OUT)); \
		uv run python scripts/extract_sections.py $(FILE) --pages $(PAGES) --output $(OUT); \
	fi

#---------------------------------------------------------------------------
# Development
#---------------------------------------------------------------------------

## Run tests
test:
	@uv run pytest tests/ -v

## Run linter
lint:
	@uv run ruff check scripts/

## Format code
format:
	@uv run ruff format scripts/

#---------------------------------------------------------------------------
# Cleanup
#---------------------------------------------------------------------------

## Clean generated files and caches
clean:
	@echo "$(BLUE)Cleaning generated files...$(RESET)"
	rm -rf __pycache__ .pytest_cache .ruff_cache
	rm -rf scripts/__pycache__
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "$(GREEN)Clean complete.$(RESET)"

## Clean working directory (intermediate files)
clean-working:
	@echo "$(YELLOW)Cleaning .working/ directory...$(RESET)"
	rm -rf .working/*
	@echo "$(GREEN)Working directory cleaned.$(RESET)"

## Clean everything including venv and working directory
clean-all: clean clean-working
	@echo "$(YELLOW)Removing virtual environment...$(RESET)"
	rm -rf .venv
	@echo "$(GREEN)Full clean complete.$(RESET)"

#---------------------------------------------------------------------------
# Help
#---------------------------------------------------------------------------

## Show this help message
help:
	@echo ""
	@echo "$(BLUE)Comparable Analysis Project$(RESET)"
	@echo "=============================="
	@echo ""
	@echo "$(GREEN)Setup Commands:$(RESET)"
	@echo "  make setup        - Full setup: install uv, create venv, install deps"
	@echo "  make install      - Install dependencies only"
	@echo "  make install-dev  - Install dev dependencies"
	@echo ""
	@echo "$(GREEN)Document Processing:$(RESET)"
	@echo "  make check        - Check all document sizes in dataroom/"
	@echo "  make check-file FILE=path/to/file.pdf"
	@echo "                    - Check specific file size"
	@echo "  make guide        - Show 10-K section guide"
	@echo "  make strategies   - Show chunking strategies"
	@echo "  make pdf-info FILE=path/to/file.pdf"
	@echo "                    - Get PDF page count and info"
	@echo "  make extract-pages FILE=path PAGES=80-120 [OUT=.working/...]"
	@echo "                    - Extract pages from PDF to .working/ (default)"
	@echo ""
	@echo "$(GREEN)Development:$(RESET)"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linter"
	@echo "  make format       - Format code"
	@echo ""
	@echo "$(GREEN)Cleanup:$(RESET)"
	@echo "  make clean        - Clean caches and pyc files"
	@echo "  make clean-working - Clean .working/ directory"
	@echo "  make clean-all    - Clean everything including venv"
	@echo ""
	@echo "$(GREEN)Examples:$(RESET)"
	@echo "  make setup"
	@echo "  make check"
	@echo "  make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120"
	@echo "    # Outputs to: .working/nota/nota-sec-80-120.txt (auto-named)"
	@echo ""
	@echo "$(GREEN)Directory Structure:$(RESET)"
	@echo "  dataroom/   - Source documents (input)"
	@echo "  .working/   - Intermediate files (pre-extracted text)"
	@echo "  output/     - Final analysis outputs and reports"
	@echo ""
