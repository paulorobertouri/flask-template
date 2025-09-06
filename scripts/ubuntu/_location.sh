# About: This script is used to change the current directory to the root of the project.
# shellcheck shell=ksh

location=$(pwd)

if [[ $location == *"/scripts/ubuntu"* ]]; then
    echo "Changing directory to root..."
    cd ../../
fi
