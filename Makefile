SHELL := /bin/bash

PYTHON_VERSION := python3

VENV_DIR := .venv

install:
	./scripts/ubuntu/install.sh

test:
	./scripts/ubuntu/test.sh

run:
	./scripts/ubuntu/run.sh

cleanup:
	./scripts/ubuntu/cleanup.sh

uninstall:
	./scripts/ubuntu/uninstall.sh

check:
	./scripts/ubuntu/check.sh

upgrade:
	./scripts/ubuntu/upgrade.sh

pre-commit-install:
	./scripts/ubuntu/install-pre-commit.sh
