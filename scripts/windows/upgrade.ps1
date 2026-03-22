# About: This script is used to configure a development environment.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

Write-Host "Upgrading dependencies" -ForegroundColor Green

uv sync --upgrade

Write-Host "Done" -ForegroundColor Green
