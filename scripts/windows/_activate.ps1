if (-not (Test-Path .venv)) {
	.\scripts\windows\install.ps1
}

Write-Host "Activating Python virtual environment" -ForegroundColor Green

.venv\Scripts\Activate.ps1
