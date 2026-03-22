SHELL := /bin/bash

install:
	uv sync --no-dev

install-dev:
	uv sync

test:
	uv run pytest --cov --cov-report=html --cov-report=term --cov-report=term-missing

run:
	uv run python main.py

cleanup:
	./scripts/ubuntu/cleanup.sh

uninstall:
	./scripts/ubuntu/uninstall.sh

check:
	uv run pre-commit run --all-files

upgrade:
	uv sync --upgrade

pre-commit-install:
	uv run pre-commit install

docker-curl-test:
	bash tests/docker/test_with_curl.sh
