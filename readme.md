# Python Web Template

This project showcases example of a web application with tests.

This project can be used as a template for new Python projects, providing a structured layout and examples of unit tests for different scenarios and functionalities. By exploring the examples and best practices in this project, you can learn how to write effective unit tests and improve the quality of your codebase.

## How to Run the Application

To run the application, you can use the following command:

```bash
make run
```

Or using scripts (Ubuntu):

```bash
./scripts/ubuntu/run.sh
```

Or using scripts (Windows):

```bash
./scripts/windows/run.ps1
```

## How to Run the Tests

To run the tests with coverage measurement, you can use the following command:

```bash
make test
```

Or using scripts (Ubuntu):

```bash
./scripts/ubuntu/test.sh
```

Or using scripts (Windows):

```bash
./scripts/windows/test.ps1
```

## How to Run the Linters

To run the linters, you can use the following command:

```bash
make check
```

Or using scripts (Ubuntu):

```bash
./scripts/ubuntu/check.sh
```

Or using scripts (Windows):

```bash
./scripts/windows/check.ps1
```

## References

- [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://docs.pytest.org/en/latest/)
- [flask](https://flask.palletsprojects.com/en/latest/)

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
