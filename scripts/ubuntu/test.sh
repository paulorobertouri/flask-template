#!/bin/bash

# About: This script is used to run the project on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

uv sync

source ./scripts/ubuntu/_activate.sh

echo "Running tests"

python3 -m pytest --cov --cov-report=html --cov-report=term --cov-report=term-missing
