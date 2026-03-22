#!/bin/bash

# About: This script is used to configure a development environment.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

echo "Installing all dependencies with uv"

uv sync

echo "Done."
