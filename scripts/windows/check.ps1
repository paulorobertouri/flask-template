# About: This script is used to run pre-commit checks.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\install-dev.ps1

Write-Host "Running pre-commit checks" -ForegroundColor Green

pre-commit run --all-files

Write-Host "Done" -ForegroundColor Green
