#!/bin/bash

# About: This script is used to install the project dependencies on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment"

    python3 -m venv .venv
fi

echo "Activating Python virtual environment"

# shellcheck source=/dev/null
. ./.venv/bin/activate

echo "Installing project dependencies"

python3 -m pip install -r requirements.txt

echo "Done"
