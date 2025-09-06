# About: This script is used to install the project dependencies on Windows.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

Clear-Host

if (-not (Test-Path .venv)) {
	Write-Host "Creating Python virtual environment" -ForegroundColor Green

	python -m venv .venv
}

Write-Host "Activating Python virtual environment" -ForegroundColor Green

.venv\Scripts\Activate.ps1

Write-Host "Installing project dependencies" -ForegroundColor Green

python -m pip install -r requirements.txt

Write-Host "Done" -ForegroundColor Green
