# About: This script is used to test the project on Windows.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\install-dev.ps1

Write-Host "Running tests" -ForegroundColor Green

python -m pytest --cov --cov-report=html --cov-report=term --cov-report=term-missing
