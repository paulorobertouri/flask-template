# Flask Template

Flask API template with service/repository layering, JWT authentication, Swagger docs, and test coverage.

## Stack

- Flask + Flasgger
- PyJWT + python-dotenv
- Ruff + mypy
- Pytest + coverage
- uv (package manager)

## Commands

- `make install` - Install dependencies
- `make install-dev` - Install dev dependencies
- `make run` - Run the application
- `make test` - Run tests with coverage
- `make check` - Run linters and type checkers
- `make docker-build` - Build Docker image
- `make docker-test` - Run tests in Docker
- `make docker-curl-test` - Run curl integration tests in Docker

## Endpoints

- GET /docs - Swagger documentation
- GET /health - Health check
- GET /v1/public - Public endpoint
- GET /v1/customer - Customer list endpoint
- GET /v1/auth/login - Login endpoint (returns JWT)
- GET /v1/private - Protected endpoint (requires Authorization header)

## JWT Contract

Login returns:
- Body: {"token":"..."}
- Header: Authorization: Bearer <token>
- Header: X-JWT-Token: <token>

## Environment Variables

- PORT=8000
- JWT_SECRET=your-super-secret-jwt-key-at-least-32-characters-long-for-hs256
- JWT_ALGORITHM=HS256
- JWT_EXPIRY_MINUTES=60
- FLASK_ENV=development

## Project Structure

```text
.
├── main.py                 # Entry point (ASGI wrapper with Uvicorn)
├── app/
│   ├── __init__.py        # Flask app setup
│   ├── api/
│   │   └── v1_routes.py   # API route handlers
│   ├── services/          # Business logic
│   ├── repositories/      # Data access abstraction
│   └── domain/            # Domain models
├── tests/
│   ├── e2e/               # Integration/E2E tests
│   ├── unit/              # Unit tests
│   └── docker/            # Docker acceptance tests
└── docker/
    ├── build.Dockerfile   # Production image
    └── test.Dockerfile    # Test image
```

## Architecture

- `app/services`: business services
- `app/repositories`: data-access abstractions
- `app/domain`: domain models
- `tests`: unit and e2e suites

## Shared Template Contract

All Python templates in this repository follow the same quality contract.

### Functional Contract

- Keep business logic in service/domain modules.
- Keep transport/web concerns at API route layer.
- Keep tests split into fast unit tests and integration/e2e tests where applicable.

### Quality Gates

- Lint must pass.
- Typecheck must pass.
- Test suite must pass.
- Coverage report must be generated on test runs.

### Architecture Contract

- Domain and service logic isolated from framework wiring.
- Repository or adapter boundaries for persistence/integration concerns.
- Testable composition with deterministic defaults.
