# About: This script is used to install pre-commit hooks.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\install-dev.ps1

Write-Host "Installing pre-commit hooks" -ForegroundColor Green

pre-commit install

mypy --install-types --non-interactive

Write-Host "Done" -ForegroundColor Green
