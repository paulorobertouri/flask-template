#!/bin/bash

# About: This script is used to install the project dependencies on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

echo "Installing project dependencies with uv"

uv sync --no-dev

echo "Done"
