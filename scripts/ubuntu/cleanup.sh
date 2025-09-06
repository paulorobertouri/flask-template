#!/bin/bash

# About: This script is used to clean up a virtual environment.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

if [ -d "build" ]; then
    echo "Removing build directory"
    rm -rf "build"
fi

if [ -d "dist" ]; then
    echo "Removing dist directory"
    rm -rf "dist"
fi

if [ -d "htmlcov" ]; then
    echo "Removing htmlcov directory"
    rm -rf "htmlcov"
fi

if [ -f "coverage.xml" ]; then
    echo "Removing coverage.xml file"
    rm -f "coverage.xml"
fi

if [ -f ".coverage" ]; then
    echo "Removing .coverage file"
    rm -f ".coverage"
fi

if [ -d ".mypy_cache" ]; then
    echo "Removing .mypy_cache directory"
    rm -rf ".mypy_cache"
fi

if [ -f "md_report.md" ]; then
    echo "Removing md_report.md file"
    rm -f "md_report.md"
fi

echo "Removing __pycache__ directories"
find . -type d -name "__pycache__" -. rm -rf {} +

echo "Removing .pytest_cache directories"
find . -type d -name ".pytest_cache" -. rm -rf {} +

echo "Removing .promptflow directories"
find . -type d -name ".promptflow" -. rm -rf {} +
