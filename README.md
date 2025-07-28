# FastAPI Recipes Backend

A production-ready, type-safe FastAPI backend for saving and managing recipes, with user authentication and modern best practices.

## Features
- FastAPI with full type annotations
- User authentication (OAuth2, JWT, fastapi-users)
- SQLAlchemy ORM and Alembic migrations
- Pydantic schemas for validation
- Dockerized for easy development
- Pre-commit hooks, linting, formatting, and CI

## Quick Start

1. Clone the repo
2. Create and activate a Python virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
4. Copy .env.example to .env and update secrets (or create .env manually)
5. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
6. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

## Project Structure
See PLANNED_STRUCTURE.md for details.

## Code Quality
- Run `pre-commit install` to enable hooks for formatting, linting, and type checks.
- Run `black .`, `isort .`, `flake8 .`, and `mypy .` manually as needed.

## Testing
- Run tests with:
  ```bash
  pytest
  ```

## CI
- All pushes and pull requests are checked with GitHub Actions for tests, lint, and type checks.

## Contributing
- Ensure all code is type-annotated and covered by tests.
- Follow the code style enforced by pre-commit hooks.
- Update documentation as needed.
