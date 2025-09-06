#!/bin/bash

# About: This script is used to run pre-commit checks.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

bash ./scripts/ubuntu/install-dev.sh

source ./scripts/ubuntu/_activate.sh

echo "Running pre-commit checks..."

pre-commit run --all-files

echo "Done."
