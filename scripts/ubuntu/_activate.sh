# About: Activates the Python virtual environment
# shellcheck shell=ksh

if [ ! -d .venv ]; then
    echo "Creating virtual environment with uv"
    uv sync
fi

echo "Activating Python virtual environment"

# shellcheck source=/dev/null
. ./.venv/bin/activate
