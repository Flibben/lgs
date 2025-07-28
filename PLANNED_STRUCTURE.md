# Planned Project Structure

```
lgs/
│
├── app/                        # Main application package
│   ├── __init__.py
│   ├── main.py                 # FastAPI app instance and entrypoint
│   ├── api/                    # API route definitions
│   │   ├── __init__.py
│   │   └── v1/                 # Versioned API (v1)
│   │       ├── __init__.py
│   │       ├── recipes.py      # Recipe endpoints
│   │       └── users.py        # User endpoints
│   ├── core/                   # Core settings, config, security
│   │   ├── __init__.py
│   │   ├── config.py           # Settings, environment variables
│   │   ├── security.py         # Auth/JWT logic
│   │   └── logging.py          # Logging setup
│   ├── models/                 # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── recipe.py
│   ├── schemas/                # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── recipe.py
│   ├── db/                     # Database session, init, migrations
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── services/               # Business logic/services
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── recipe_service.py
│   └── dependencies/           # Dependency injection
│       ├── __init__.py
│       └── auth.py
│
├── alembic/                    # Alembic migrations
│   └── versions/
│
├── tests/                      # Test suite (pytest)
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_recipes.py
│   └── test_users.py
│
├── .env                        # Environment variables (not in VCS)
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Dev/test dependencies
├── Dockerfile                  # Docker image definition
├── docker-compose.yml          # For local dev (DB, etc.)
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .flake8                     # Flake8 config
├── pyproject.toml              # Black, isort, mypy config
├── README.md                   # Project overview
└── PLANNED_STRUCTURE.md        # This file
```

## Notes
- All code is type-annotated.
- All endpoints, models, and schemas are versioned and organized.
- Dev tools and configs are included for formatting, linting, and type checking.
- Tests are organized by feature.
- Docker and environment management are included.
