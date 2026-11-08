"""AC 1: an isolated Python 3.12+ environment created with uv."""

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_python_is_3_12_or_newer() -> None:
    assert sys.version_info >= (3, 12), f"running Python {sys.version.split()[0]}; need 3.12+"


def test_tests_run_inside_a_virtual_environment() -> None:
    assert sys.prefix != sys.base_prefix, (
        "not running inside a virtual environment. Run `uv sync`, then use `uv run pytest`."
    )


def test_pyproject_declares_python_3_12_or_newer() -> None:
    data = tomllib.loads((ROOT / "pyproject.toml").read_text())
    requires = data["project"]["requires-python"]
    match = re.search(r">=\s*3\.(\d+)", requires)
    assert match is not None and int(match.group(1)) >= 12, f"requires-python is {requires!r}"


def test_python_version_is_pinned_for_uv() -> None:
    assert (ROOT / ".python-version").read_text().strip(), ".python-version must not be empty"


def test_lockfile_is_committed() -> None:
    assert (ROOT / "uv.lock").is_file(), "uv.lock is missing: run `uv sync` and commit the lockfile"


def test_virtual_environment_is_not_committed() -> None:
    gitignore = (ROOT / ".gitignore").read_text().splitlines()
    ignored = any(line.strip().rstrip("/") == ".venv" for line in gitignore)
    assert ignored, ".venv must be in .gitignore"
