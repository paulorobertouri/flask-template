#!/bin/bash

# About: This script is used to clean up a virtual environment.

function remove_items() {
    local directories=("$@")
    for directory in "${directories[@]}"; do
        echo -e "\e[32mRemoving $directory directories\e[0m"
        find . -type d -name "$directory" -exec rm -rf {} +
    done
}

function remove_files() {
    local files=("$@")
    for file in "${files[@]}"; do
        echo -e "\e[32mRemoving $file files\e[0m"
        find . -type f -name "$file" -exec rm -f {} +
    done
}

directories_to_remove=(
    "bin"
    "build"
    "dist"
    "htmlcov"
    ".mypy_cache"
    "__pycache__"
    ".pytest_cache"
    ".promptflow"
    ".benchmarks"
    ".cache"
    ".output"
    ".dump"
    ".data"
    ".test"
    ".py-venv"
    ".venv"
    "node_modules"
    ".next"
)

files_to_remove=(
    "coverage.xml"
    ".coverage"
    "md_report.md"
)

remove_items "${directories_to_remove[@]}"
remove_files "${files_to_remove[@]}"

echo -e "\e[32mCleaning up npm cache\e[0m"
npm cache clean --force

echo -e "\e[32mCleaning up pip cache\e[0m"
pip cache purge

echo -e "\e[32mCleaning up docker containers\e[0m"
docker system prune -a --volumes -f

echo -e "\e[32mDone cleaning up\e[0m"
