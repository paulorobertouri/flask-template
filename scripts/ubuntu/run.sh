#!/bin/bash

# About: This script is used to run the project on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

source ./scripts/ubuntu/_activate.sh

echo "Running the project"

python3 ./main.py
