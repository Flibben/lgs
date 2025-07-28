# Project TODO Checklist

- [x] Initialize a git repository
- [x] Set up a Python virtual environment
- [x] Create the project folder structure as per PLANNED_STRUCTURE.md
- [ ] Add .env, .gitignore, and initial README.md
    - [x] .gitignore
    - [x] .env
    - [x] initial README.md

- [x] Create requirements.txt and requirements-dev.txt with all dependencies
- [x] Set up black, isort, flake8, mypy, and pre-commit configuration files
- [x] Add pyproject.toml for unified tool configuration
- [x] Set up Dockerfile and docker-compose.yml for local development and deployment

- [x] Scaffold FastAPI app in app/main.py
- [x] Set up app/core/config.py for environment/config management
- [x] Set up app/core/logging.py for logging configuration
- [x] Set up app/db/session.py and app/db/base.py for SQLAlchemy session and base model

- [x] Integrate fastapi-users for user registration, login, and JWT authentication
- [x] Set up app/models/user.py and app/schemas/user.py for user models and schemas
- [x] Configure app/core/security.py for JWT and password hashing
- [x] Set up app/dependencies/auth.py for authentication dependencies

- [x] Create app/models/recipe.py and app/schemas/recipe.py for recipe data
- [x] Implement app/services/recipe_service.py for recipe business logic
- [x] Add app/api/v1/recipes.py for recipe endpoints

- [ ] Set up Alembic for migrations
- [ ] Create initial migration for user and recipe tables

- [ ] Set up tests/ directory with conftest.py, test_users.py, and test_recipes.py
- [ ] Write tests for user registration, login, and recipe CRUD

- [ ] Set up pre-commit hooks for formatting, linting, and type checks
- [ ] Add CI configuration (e.g., GitHub Actions) for tests, linting, and type checks

- [ ] Update README.md with setup, usage, and contribution instructions
- [ ] Review and finalize all configs and code for production readiness