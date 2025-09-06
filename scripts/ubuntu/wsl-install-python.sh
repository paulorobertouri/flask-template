#!/bin/bash

# About: This script is used to install the project dependencies on Linux.

if [ -f "_location.sh" ]; then
    # shellcheck source=./scripts/ubuntu/_location.sh
    source ./_location.sh
fi

clear

sudo add-apt-repository universe
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
sudo apt-get install -y python3-venv
