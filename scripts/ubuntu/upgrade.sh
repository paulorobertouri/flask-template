#!/bin/bash

# About: This script is used to configure a development environment.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

echo "Upgrading dependencies"

uv sync --upgrade

echo "Done."
