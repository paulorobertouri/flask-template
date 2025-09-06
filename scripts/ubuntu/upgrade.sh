#!/bin/bash

# About: This script is used to configure a development environment.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

source ./scripts/ubuntu/_activate.sh

echo "Installing development dependencies"

python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt --upgrade

python3 -m pip install -r requirements_dev.txt --upgrade
