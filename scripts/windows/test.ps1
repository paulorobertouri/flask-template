$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $ScriptDir)

Set-Location $ProjectRoot

Write-Output "Running tests..."
uv sync
Write-Output "Running tests..."
uv run pytest --cov --cov-report=html --cov-report=term --cov-report=term-missing
