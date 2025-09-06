# About: This script is used to run the project on Windows.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\_activate.ps1

Write-Host "Running the project" -ForegroundColor Green

python .\main.py
