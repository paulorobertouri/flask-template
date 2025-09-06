# About: Activates the Python virtual environment
# shellcheck shell=ksh

if [ ! -d .venv ]; then
    bash ./scripts/ubuntu/install.sh
fi

echo "Activating Python virtual environment"

# shellcheck source=/dev/null
. ./.venv/bin/activate
