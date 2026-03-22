#!/bin/bash

set -euo pipefail

echo "Installing project dependencies with uv"
uv sync --no-dev

echo "Done"
