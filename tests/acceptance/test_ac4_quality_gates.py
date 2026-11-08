"""AC 4: the domain function is tested, and the whole toolchain is green.

`ruff`, `mypy` and `pytest` (this very run) must all succeed. The tests in tests/test_pricing.py
cover the domain function itself.
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def _run(*args: str) -> None:
    result = subprocess.run(  # noqa: S603 - fixed argument list, no shell
        [sys.executable, "-m", *args], cwd=ROOT, capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, f"`{' '.join(args)}` failed:\n{result.stdout}\n{result.stderr}"


def test_domain_pricing_module_exists() -> None:
    pricing = ROOT / "domain" / "pricing.py"
    assert pricing.is_file(), "implement apply_discount in domain/pricing.py"


@pytest.mark.parametrize("args", [("ruff", "check", "."), ("ruff", "format", "--check", ".")])
def test_ruff_is_clean(args: tuple[str, ...]) -> None:
    _run(*args)


def test_mypy_strict_is_clean() -> None:
    _run("mypy", ".")
