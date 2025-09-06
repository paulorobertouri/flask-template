# About: This script is used to uninstall the project dependencies on Windows.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

.\scripts\windows\cleanup.ps1

if (-not (Test-Path .\.venv)) {
	Write-Host "Python virtual environment not found" -ForegroundColor Yellow
	return
}

try {
	Write-Host "Try uninstalling pre-commit" -ForegroundColor Green

	pre-commit uninstall
}
catch {
	Write-Host "Failed to uninstall pre-commit" -ForegroundColor Yellow
}

Write-Host "Uninstalling project dependencies" -ForegroundColor Green

if (Test-Path .venv\Scripts\Deactivate.ps1) {
	.venv\Scripts\Deactivate.ps1
}

Write-Host "Uninstalling project dependencies" -ForegroundColor Green

python -m pip uninstall -r requirements.txt -y

Write-Host "Uninstalling development dependencies" -ForegroundColor Green

python -m pip uninstall -r requirements_dev.txt -y

if (Test-Path .\.venv) {
	Write-Host "Removing Python virtual environment" -ForegroundColor Green
	Remove-Item -Path .\.venv -Recurse -Force
}

if (Test-Path .\venv) {
	Write-Host "Removing Python virtual environment" -ForegroundColor Green
	Remove-Item -Path .\.venv -Recurse -Force
}
