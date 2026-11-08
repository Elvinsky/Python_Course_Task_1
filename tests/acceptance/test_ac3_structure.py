"""AC 3: /config, /domain, /api and /tests are separate packages; /domain stays framework-free."""

import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PACKAGES = ["config", "domain", "api", "tests"]
FRAMEWORKS = {"fastapi", "starlette", "sqlalchemy", "pydantic", "flask", "django", "uvicorn"}


@pytest.mark.parametrize("package", PACKAGES)
def test_package_exists(package: str) -> None:
    directory = ROOT / package
    assert directory.is_dir(), f"create the /{package} directory"
    assert (directory / "__init__.py").is_file(), f"add /{package}/__init__.py"


def test_domain_does_not_import_frameworks() -> None:
    offenders: list[str] = []
    for path in (ROOT / "domain").rglob("*.py"):
        for node in ast.walk(ast.parse(path.read_text())):
            names: list[str] = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            for name in names:
                if name.split(".")[0] in FRAMEWORKS:
                    offenders.append(f"{path.relative_to(ROOT)} imports {name}")
    assert not offenders, "framework imports found in /domain:\n" + "\n".join(offenders)
