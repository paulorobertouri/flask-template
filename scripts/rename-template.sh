#!/bin/bash
# Usage: ./scripts/rename-template.sh <new-name>
# Renames the template project to a new name throughout the codebase.

if [ -z "$1" ]; then
  echo "Usage: $0 <new-name>"
  exit 1
fi

NEW_NAME="$1"

# Replace in README and docs
find . -type f \( -name '*.md' -o -name '*.toml' -o -name '*.py' \) -exec sed -i "s/flask-template/$NEW_NAME/g" {} +

# Optionally update other files as needed

echo "Renamed project to $NEW_NAME. Please review and update any remaining references manually."
