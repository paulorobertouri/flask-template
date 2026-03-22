# About: This script is used to install the project dependencies on Windows.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

Write-Host "Installing project dependencies with uv" -ForegroundColor Green

uv sync --no-dev

Write-Host "Done" -ForegroundColor Green
