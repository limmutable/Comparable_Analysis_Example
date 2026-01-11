# Comparable Analysis Project Makefile
#
# Usage:
#   make setup  - Install uv and project dependencies
#   make test   - Run tests
#   make clean  - Clean up cache files

.PHONY: setup test clean help

.DEFAULT_GOAL := help

## Full project setup: install uv, create venv, install dependencies
setup:
	@echo "Checking for uv..."
	@if ! command -v uv &> /dev/null; then \
		echo "Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		echo "uv installed. Please restart your terminal or run: source ~/.bashrc"; \
	else \
		echo "uv is already installed: $$(uv --version)"; \
	fi
	@echo "Setting up project..."
	uv venv
	uv pip install -e ".[dev]"
	@echo ""
	@echo "Setup complete!"
	@echo ""
	@echo "To activate the virtual environment:"
	@echo "  source .venv/bin/activate"

## Run tests
test:
	@uv run pytest tests/ -v

## Clean up cache files
clean:
	@rm -rf __pycache__ .pytest_cache .ruff_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned up cache files"

## Show help
help:
	@echo ""
	@echo "Comparable Analysis Project"
	@echo "==========================="
	@echo ""
	@echo "  make setup  - Install uv, create venv, install dependencies"
	@echo "  make test   - Run tests"
	@echo "  make clean  - Clean up cache files"
	@echo ""
