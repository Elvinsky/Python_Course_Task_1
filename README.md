<!--
  Generated from the Python Kick-Start course: the description and acceptance criteria match the
  task window of the course app. Do not edit by hand; changes are made in the course repository.
-->

# Practical Task 1: Environment & Project Boilerplate Setup

> Part of **Python Kick-Start**: Section 1: Foundational Knowledge & Engineering Practices (4–5 Days). This repository is a **forkable starting point**:
> fork it, clone your fork, and build the task.

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

# then lint, type-check and test your work
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
4. Build the task step by step and commit small steps. Run `make check` before every push so you always know where you stand.

## 3. Task description

Bootstrap a reproducible, strictly-typed Python project skeleton. Every later task builds on this layout, so the goal is a clean machine-to-machine setup (one command to install, one command to lint, one command to test) and a folder structure that keeps business logic independent of any web framework. A small, tested domain function proves the whole toolchain works end to end. You start from a nearly empty fork of the template repository (see below) and create the configuration, the packages and the code yourself. Set up the virtual environment first, before you edit anything.

## 4. What already exists in this repository

- `.python-version`: pins Python 3.14 for uv
- `pyproject.toml`: only the `[project]` table (name, version, `requires-python >= 3.12`, no dependencies)
- `Makefile`: `make setup`, `make lint`, `make typecheck`, `make test`, `make check` and `make fmt`; they work once you have added the tools and your first tests
- `.gitignore` for Python projects (`.venv`, caches, `.env`)

Everything else is yours to create. Until you have added the tools and written your first Python files and tests,
`make typecheck` and `make test` fail (Mypy and pytest find nothing to check): that is expected.

## 5. What you need to do (acceptance criteria)

- [ ] **AC 1**: Create the virtual environment with `uv` (Python 3.12+; 3.14 is pinned), add `ruff`, `mypy` and `pytest` as development dependencies, and commit the generated `uv.lock`.
- [ ] **AC 2**: Configure `pyproject.toml`: Ruff (line length, `target-version`, lint rules including at least `E`, `F` and `I`, and the formatter) and Mypy with `strict = true`; point pytest at the `tests` directory.
- [ ] **AC 3**: Create the directory structure separating `/config`, `/domain`, `/api` and `/tests`, each an importable package; `/domain` imports no web or database framework.
- [ ] **AC 4**: Add one pure function in `/domain` with parametrized `pytest` tests in `/tests`; `make check` (Ruff, Ruff format check, Mypy strict, pytest) passes from a clean clone.

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
- Mypy (strict) or Pyright: pick one as the type-check gate in `make check`; Pylance/Pyright gives faster editor feedback
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

- [ ] every acceptance criterion above is met
- [ ] `make check` is green
- [ ] `uv.lock` and your `pyproject.toml` configuration are committed; `.venv` is not
