.DEFAULT_GOAL := check
.PHONY: setup lint typecheck test check fmt

setup:            ## create the virtual environment (.venv) and install everything
	uv python install 3.14
	uv sync

lint:             ## style and static checks
	uv run ruff check .
	uv run ruff format --check .

typecheck:        ## strict type checks
	uv run mypy .

test:             ## acceptance tests + your own tests
	uv run pytest

check: lint typecheck test   ## everything: this is the definition of "green"

fmt:              ## auto-fix what can be fixed
	uv run ruff check --fix .
	uv run ruff format .
