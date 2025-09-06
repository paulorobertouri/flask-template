#!/bin/bash

# About: This script is used to uninstall the project dependencies on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

./scripts/ubuntu/cleanup.sh

if [ ! -d ".venv" ]; then
    echo "Python virtual environment not found. Exiting..."
    exit 1
fi

source ./scripts/ubuntu/_activate.sh

echo "Try uninstalling pre-commit"

pre-commit uninstall

echo "Uninstalling project dependencies"

pip uninstall -r requirements.txt -y

echo "Uninstalling development dependencies"

pip uninstall -r requirements_dev.txt -y

if [ -d ".venv" ]; then
    echo "Removing Python virtual environment"
    rm -rf .venv
fi
