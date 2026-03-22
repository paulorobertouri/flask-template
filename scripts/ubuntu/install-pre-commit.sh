#!/bin/bash

# About: This script is used to install pre-commit hooks.

if [ -f "_location.sh" ]; then
	# shellcheck source=./scripts/ubuntu/_location.sh
	source ./_location.sh
fi

clear

uv sync

source ./scripts/ubuntu/_activate.sh

echo "Installing pre-commit hooks"

pre-commit install

echo "Done."
