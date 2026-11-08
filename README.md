<!--
  Generated from the Python Kick-Start course: the description and acceptance criteria match the
  task window of the course app. Do not edit by hand; changes are made in the course repository.
-->

# Practical Task 1: Environment & Project Boilerplate Setup

> Part of **Python Kick-Start**: Section 1: Foundational Knowledge & Engineering Practices (4–5 Days). This repository is a **forkable template**:
> fork it, clone your fork, and implement everything marked `TODO` until all acceptance tests pass.

## 1. Set up your virtual environment first

> **Do this before you touch any code.** Every task in the course runs inside an isolated virtual
> environment, so dependencies never leak into your system Python (there is no `node_modules`-style
> implicit lookup in Python). Nothing in this repository is guaranteed to work outside it.

You need [git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/getting-started/installation/)
(a fast package and environment manager that also installs Python for you).

```bash
# install uv once: https://docs.astral.sh/uv/getting-started/installation/
uv python install 3.14
uv sync
uv add --dev ruff mypy pytest
uv run python --version

# then run every acceptance check (they fail until you finish the task)
make check
```

What these commands do:

- `uv python install 3.14` downloads Python 3.14 (the version pinned in `.python-version`). Python 3.12 is the
  minimum the acceptance criteria allow; use 3.13 only if a dependency has no wheels for 3.14 yet.
- `uv sync` creates the `.venv` folder and installs the locked dependencies into it.
- `uv run <command>` always runs inside that environment, so you do not have to activate it. If you prefer to
  activate it: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows).
- `uv run python --version` must print `Python 3.14.x` (or at least 3.12). If it prints another version, stop and fix
  the environment before continuing.

Common problems:

- `uv: command not found`: install uv and open a new terminal.
- Wrong Python version: run `uv python list` and `uv python install 3.14`, then delete `.venv` and run `uv sync` again.
- `make: command not found` (Windows): run the commands from the `Makefile` by hand, or use WSL / Git Bash.

## 2. Fork, clone and work on your fork

1. **Fork** [Python_Course_Task_1](https://github.com/Elvinsky/Python_Course_Task_1) to your own GitHub account (the *Fork* button, top right).
2. **Clone your fork** (not this repository):

   ```bash
   git clone https://github.com/<your-username>/Python_Course_Task_1.git
   cd Python_Course_Task_1
   ```

3. Set up the virtual environment (section 1), then create a branch: `git switch -c solution`.
4. Search for `TODO` to find everything you have to implement: `grep -rn "TODO" . --exclude-dir=.venv --exclude-dir=.git --exclude=README.md`.
5. Commit small steps. The GitHub Actions workflow in `.github/workflows/ci.yml` runs the same checks as `make check`
   on every push to your fork, so you can see your progress there too.
6. Keep the acceptance tests in `tests/acceptance/` unchanged: they are the definition of "done" for each
   acceptance criterion. Write your own tests next to them.

## 3. Task description

Bootstrap a reproducible, strictly-typed Python project skeleton. Every later task builds on this layout, so the goal is a clean machine-to-machine setup (one command to install, one command to lint, one command to test) and a folder structure that keeps business logic independent of any web framework. A small, tested domain function proves the whole toolchain works end to end. You work in a fork of the template repository: it ships the acceptance tests, a `Makefile` and CI, and leaves the project configuration and the code for you to write. Set up the virtual environment first, before you edit anything.

## 4. Acceptance criteria

- [ ] **AC 1**: Initialize an isolated Python 3.12+ environment using `uv`.
- [ ] **AC 2**: Configure `pyproject.toml` with `Ruff` linter rules and `Mypy` strict type checks.
- [ ] **AC 3**: Create directory structure separating `/config`, `/domain`, `/api`, and `/tests`.
- [ ] **AC 4**: Add one pure function in `/domain` with parametrized `pytest` tests; `ruff check`, `ruff format --check`, `mypy .` and `pytest` all pass from a clean clone.

## 5. What the template gives you, and what is yours

| Path | State | Purpose |
|---|---|---|
| `.python-version` | provided | pins the Python version for uv (3.14) |
| `pyproject.toml` | **TODO (AC 1, AC 2)** | only the `[project]` table exists: add dev tools and configure Ruff, Mypy and pytest |
| `Makefile` | provided | `make setup`, `make lint`, `make typecheck`, `make test`, `make check` |
| `.github/workflows/ci.yml` | provided | runs the same checks on every push to your fork |
| `config/`, `domain/`, `api/` | **TODO (AC 3)** | create these packages (each with `__init__.py`); `domain/` must not import any framework |
| `domain/pricing.py` | **TODO (AC 4)** | implement `apply_discount(price: Decimal, percent: int) -> Decimal` |
| `tests/test_pricing.py` | provided | the tests your function has to satisfy; add your own parametrized tests beside it |
| `tests/acceptance/` | provided, do not edit | one file per acceptance criterion |

### How the acceptance tests map to the criteria

| Criterion | Checked by |
|---|---|
| AC 1 | `tests/acceptance/test_ac1_environment.py`: Python 3.12+, running inside a virtual environment, `uv.lock` committed, `.venv` ignored |
| AC 2 | `tests/acceptance/test_ac2_tooling_config.py`: dev group, Ruff rules, Mypy `strict = true`, pytest `testpaths` |
| AC 3 | `tests/acceptance/test_ac3_structure.py`: the four packages exist, `/domain` imports no framework |
| AC 4 | `tests/test_pricing.py` and `tests/acceptance/test_ac4_quality_gates.py`: `ruff check`, `ruff format --check` and `mypy .` all pass |

Run everything with `make check`. At the start it fails on purpose; it is green when you are done.

### `apply_discount` contract

- `apply_discount(Decimal("100.00"), 0) == Decimal("100.00")`
- `apply_discount(Decimal("19.99"), 10) == Decimal("17.99")` (round to 2 decimal places with `quantize`)
- A `percent` outside `0..100` raises `ValueError`
- It is a pure function: no I/O, no globals, no framework imports

## 6. Tech stack requirements

- Python 3.12+
- uv
- Ruff
- Mypy (strict)
- pytest
- pyproject.toml

## 7. Recommended stack

**Python version:** Python 3.14 (current stable). Fall back to 3.13 if a tool lacks support; 3.12 is the minimum the ACs allow. Pin it with `requires-python` in `pyproject.toml` and a `.python-version` file, and let `uv python install` fetch it.

**Runtime & packaging**

- uv: installs Python, creates the venv, resolves and locks dependencies (`uv.lock`) in one tool
- pyproject.toml (PEP 621) with dependency-groups: single source of truth for metadata, dev dependencies and tool config

**Quality tooling**

- Ruff: linter, import sorter and formatter in one fast tool
- Mypy (strict) or Pyright: pick one as the CI gate; Pylance/Pyright gives faster editor feedback
- pytest + pytest-cov: tests and coverage; see the testing topic
- pre-commit (optional): runs Ruff and Mypy before each commit

**Editor**

- VS Code (Python, Pylance, Ruff extensions) or PyCharm: select the `.venv` interpreter and enable format-on-save

**Avoid**

- Global `pip install` and a hand-maintained `requirements.txt` as the source of truth
- The black + isort + flake8 combination (Ruff replaces all three)
- `setup.py`, Pipenv and conda for this project
- Importing FastAPI, SQLAlchemy or other frameworks inside `/domain`

## 8. Architecture guidelines

- `/config` reads settings from environment variables only (Twelve-Factor: config in the environment, never in code).
- `/domain` holds pure business logic: no FastAPI, SQLAlchemy or other framework imports.
- `/api` is a thin delivery layer that depends on `/domain`; the dependency never points the other way.
- `/tests` mirrors the package layout; commit `uv.lock` so installs are reproducible.
- Treat `ruff check`, `ruff format --check`, `mypy .` and `pytest` as the definition of "green" before every commit.

## 9. Study first

Topics from the Python Kick-Start roadmap for this section:

- **Python Tooling, Isolation & Code Quality**: [Python virtual environments (devfieldguide.com)](https://www.devfieldguide.com/blog/python-virtual-environments) · [uv documentation](https://docs.astral.sh/uv/) · [Ruff documentation](https://docs.astral.sh/ruff/) · [Mypy documentation](https://mypy.readthedocs.io/)
- **Python Data Model for JS Developers**: [Python tutorial: an informal introduction](https://docs.python.org/3/tutorial/introduction.html) · [Python tutorial: control flow](https://docs.python.org/3/tutorial/controlflow.html) · [Data model reference](https://docs.python.org/3/reference/datamodel.html) · [PEP 8: style guide](https://peps.python.org/pep-0008/)
- **Collections, Comprehensions & Iteration**: [Python tutorial: data structures](https://docs.python.org/3/tutorial/datastructures.html) · [collections module](https://docs.python.org/3/library/collections.html) · [itertools module](https://docs.python.org/3/library/itertools.html)
- **Functions, Decorators, Generators & Context Managers**: [Python tutorial: defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) · [functools module](https://docs.python.org/3/library/functools.html) · [contextlib module](https://docs.python.org/3/library/contextlib.html) · [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html)
- **Classes, Dataclasses & the Dunder Protocol**: [Python tutorial: classes](https://docs.python.org/3/tutorial/classes.html) · [dataclasses module](https://docs.python.org/3/library/dataclasses.html) · [Special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- **Exceptions, Files & Regex**: [Python tutorial: errors and exceptions](https://docs.python.org/3/tutorial/errors.html) · [pathlib module](https://docs.python.org/3/library/pathlib.html) · [re module](https://docs.python.org/3/library/re.html)
- **Modules, Packages & Imports**: [Python tutorial: modules](https://docs.python.org/3/tutorial/modules.html) · [The import system](https://docs.python.org/3/reference/import.html) · [Standard library index](https://docs.python.org/3/library/)
- **Type Hints & Static Typing**: [typing module](https://docs.python.org/3/library/typing.html) · [Mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) · [Pyright documentation](https://microsoft.github.io/pyright/)
- **Testing with pytest**: [pytest documentation](https://docs.pytest.org/en/stable/) · [pytest: fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [unittest module](https://docs.python.org/3/library/unittest.html)
- **IDEs & Clean Architecture**: [Altered Craft (writing.alteredcraft.com)](https://writing.alteredcraft.com/) · [The Twelve-Factor App](https://12factor.net/)

## Definition of done

- [ ] `make check` is green locally and in the CI of your fork
- [ ] `uv.lock` and your `pyproject.toml` configuration are committed, `.venv` is not
- [ ] Stretch: add a second pure function to `/domain` with its own parametrized tests
