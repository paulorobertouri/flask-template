# About: This script is used to configure a development environment.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\_activate.ps1

Write-Host "Installing development dependencies" -ForegroundColor Green

python -m pip install --upgrade pip

python -m pip install -r .\requirements.txt --upgrade

python -m pip install -r .\requirements_dev.txt --upgrade
