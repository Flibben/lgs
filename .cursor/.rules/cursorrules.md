# Tech Stack and Project Standards

## Tech Stack
- Python 3.11+
- FastAPI (web framework)
- Uvicorn (ASGI server)
- Pydantic (data validation and typing)
- SQLAlchemy (ORM for database access)
- Alembic (database migrations)
- pytest (testing)
- httpx (async HTTP client, for testing)
- mypy (static type checking)
- black (code formatting)
- isort (import sorting)
- flake8 (linting)
- pre-commit (code quality hooks)
- python-dotenv (environment variable management)

## Project Standards
- All code must be fully type-annotated.
- Use black and isort for formatting and import sorting.
- Use flake8 for linting.
- Use mypy for type checking.
- All endpoints and models must use Pydantic for validation and typing.
- All database access should go through SQLAlchemy ORM models.
- Use Alembic for database migrations.
- All code must be covered by tests using pytest.
- Use pre-commit to enforce formatting, linting, and type checking before commits.
- Store secrets and configuration in .env files, never in code or version control.
- Write clear docstrings for all public functions and classes.
- Prefer async code where possible (FastAPI, SQLAlchemy 2.0+).

## Production Readiness
- Use environment variables for configuration.
- Add logging and error handling.
- Ensure all dependencies are pinned in requirements files.
- Use Docker for local development and deployment.
- Set up CI for tests, linting, and type checks.

# Authentication & User Management

## Recommended Approach
- **Authentication Method:** Use OAuth2 with Password (and optionally Social) flows, issuing JWT (JSON Web Tokens) for stateless authentication.
- **User Management:** Use the fastapi-users package for user registration, login, password reset, and user database management. This package integrates well with FastAPI, supports JWT, and is fully type-annotated.
- **Password Security:** Use passlib for secure password hashing (fastapi-users uses this internally).
- **Token Handling:** Use python-jose for JWT encoding/decoding (fastapi-users uses this internally).
- **Protecting Endpoints:** Use FastAPI’s dependency injection to require authentication for protected routes.
- **User Models:** Store users in the database using SQLAlchemy models, with support for roles/permissions if needed.
- **Environment Variables:** Store secret keys and sensitive config in .env files.

## Tech Stack Additions
- fastapi-users (user management, authentication)
- passlib (password hashing)
- python-jose (JWT handling)

## Project Standards Additions
- All authentication must use OAuth2 with JWT tokens.
- Use fastapi-users for user registration, login, and password reset.
- Store user data in the database using SQLAlchemy models.
- Protect sensitive endpoints with authentication dependencies.
- Never store plain-text passwords; always use secure hashing.
- Store authentication secrets in environment variables.

# General guidelines

When planning a complex code change, always start with a plan of action and then ask me for approval on that plan.

For simple changes, just make the code change but always think carefully and step-by-step about the change itself.

When a function becomes too long, split it into smaller functions.

When debugging a problem, make sure you have sufficient information to deeply understand the problem.

More often than not, opt in to adding more logging and tracing to the code to help you understand the problem before making any changes. If you are provided logs that make the source of the problem obvious, then implement a solution. If you're still not 100% confident about the source of the problem, then reflect on 4-6 different possible sources of the problem, distill those down to 1-2 most likely sources, and then implement a solution for the most likely source - either adding more logging to validate your theory or implement the actual fix if you're extremely confident about the source of the problem.