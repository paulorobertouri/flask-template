#!/bin/bash

# About: This script is used to run the project on Linux.

if [ -f "_location.sh" ]; then
	# shellcheck source=./scripts/ubuntu/_location.sh
	source ./_location.sh
fi

clear

bash ./scripts/ubuntu/install-dev.sh

source ./scripts/ubuntu/_activate.sh

echo "Installing pre-commit hooks"

pre-commit install

echo "Done."
