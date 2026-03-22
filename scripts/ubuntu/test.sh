#!/usr/bin/env bash
set -euo pipefail
uv sync
uv run pytest --cov --cov-report=html --cov-report=term --cov-report=term-missing
