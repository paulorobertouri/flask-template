# About: This script is used to configure a development environment.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

Write-Host "Installing all dependencies with uv" -ForegroundColor Green

uv sync

Write-Host "Done" -ForegroundColor Green
