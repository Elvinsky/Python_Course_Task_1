"""AC 2: pyproject.toml configures Ruff lint rules and Mypy strict type checks."""

import re
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _pyproject() -> dict[str, Any]:
    return tomllib.loads((ROOT / "pyproject.toml").read_text())


def _tool(name: str) -> dict[str, Any]:
    tool = _pyproject().get("tool", {})
    assert name in tool, f"[tool.{name}] is missing in pyproject.toml"
    section: dict[str, Any] = tool[name]
    return section


def test_dev_dependencies_are_declared() -> None:
    dev = _pyproject().get("dependency-groups", {}).get("dev", [])
    names = {re.split(r"[<>=!~\[ ;]", str(d), maxsplit=1)[0].lower() for d in dev}
    missing = {"ruff", "mypy", "pytest"} - names
    assert not missing, f"dev dependency group lacks {sorted(missing)}: use `uv add --dev ...`"


def test_ruff_is_configured() -> None:
    ruff = _tool("ruff")
    assert isinstance(ruff.get("line-length"), int), "set [tool.ruff] line-length"
    target = str(ruff.get("target-version", ""))
    assert target.startswith("py3"), 'set [tool.ruff] target-version = "py312"'


def test_ruff_lint_rules_are_selected() -> None:
    select = _tool("ruff").get("lint", {}).get("select", [])
    assert {"E", "F", "I"} <= set(select), (
        f'[tool.ruff.lint] select needs "E", "F", "I"; got {select}'
    )


def test_mypy_strict_is_enabled() -> None:
    assert _tool("mypy").get("strict") is True, "set [tool.mypy] strict = true"


def test_pytest_collects_the_tests_directory() -> None:
    options = _tool("pytest").get("ini_options", {})
    testpaths = options.get("testpaths", [])
    assert "tests" in testpaths, 'set [tool.pytest.ini_options] testpaths = ["tests"]'
