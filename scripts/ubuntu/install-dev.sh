#!/bin/bash

set -euo pipefail

echo "Installing all dependencies with uv"
uv sync

echo "Done."
