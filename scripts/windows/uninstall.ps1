# About: This script is used to uninstall the project dependencies on Windows.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\cleanup.ps1

try {
	Write-Host "Try uninstalling pre-commit" -ForegroundColor Green

	pre-commit uninstall
}
catch {
	Write-Host "Failed to uninstall pre-commit" -ForegroundColor Yellow
}

if (Test-Path .\.venv) {
	Write-Host "Removing Python virtual environment" -ForegroundColor Green
	Remove-Item -Path .\.venv -Recurse -Force
}

if (Test-Path .\venv) {
	Write-Host "Removing Python virtual environment" -ForegroundColor Green
	Remove-Item -Path .\venv -Recurse -Force
}

Write-Host "Done" -ForegroundColor Green
