#!/bin/bash

# About: This script is used to uninstall the project dependencies on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

./scripts/ubuntu/cleanup.sh

if [ -d ".venv" ]; then
    echo "Removing Python virtual environment"
    rm -rf .venv
else
    echo "Python virtual environment not found. Skipping..."
fi

echo "Done."
