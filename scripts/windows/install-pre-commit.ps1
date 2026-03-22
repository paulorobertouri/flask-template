# About: This script is used to install pre-commit hooks.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

uv sync

Write-Host "Installing pre-commit hooks" -ForegroundColor Green

pre-commit install

Write-Host "Done" -ForegroundColor Green
