SHELL := /bin/bash

.PHONY: help install install-dev run test test-unit test-e2e coverage format lint docker-build docker-test

help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  run          Run the application locally"
	@echo "  test         Run all tests"
	@echo "  test-unit    Run unit tests"
	@echo "  test-e2e     Run E2E tests with Playwright"
	@echo "  coverage     Run tests with coverage report"
	@echo "  format       Format code"
	@echo "  lint         Lint code"
	@echo "  docker-build Build production docker image"
	@echo "  docker-test  Run tests inside docker"

install:
	./scripts/ubuntu/install.sh

install-dev:
	./scripts/ubuntu/install-dev.sh
	playwright install chromium

run:
	./scripts/ubuntu/run.sh

start:
	bash ./scripts/start.sh

stop:
	bash ./scripts/stop.sh

test:
	./scripts/ubuntu/test.sh

test-unit:
	pytest tests/unit

test-e2e:
	pytest tests/e2e

coverage:
	pytest --cov=app --cov-report=html tests/unit

format:
	bash ./scripts/ubuntu/format.sh

lint:
	bash ./scripts/ubuntu/lint.sh

docker-build:
	docker build -f docker/build.Dockerfile -t flask-template-build .

docker-test:
	docker build -f docker/test.Dockerfile -t flask-template-test .
	docker run --rm flask-template-test
