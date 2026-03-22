if (-not (Test-Path .venv)) {
	Write-Host "Creating virtual environment with uv" -ForegroundColor Green
	uv sync
}

Write-Host "Activating Python virtual environment" -ForegroundColor Green

.venv\Scripts\Activate.ps1
