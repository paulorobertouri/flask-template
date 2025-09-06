# About: This script is used to clean up a virtual environment.

if (Test-Path .\_location.ps1) {
	.\_location.ps1
}

if (Test-Path .\build) {
	Write-Host "Removing build directory" -ForegroundColor Green
	Remove-Item -Path .\build -Recurse -Force
}

if (Test-Path .\dist) {
	Write-Host "Removing dist directory" -ForegroundColor Green
	Remove-Item -Path .\dist -Recurse -Force
}

if (Test-Path .\htmlcov) {
	Write-Host "Removing htmlcov directory" -ForegroundColor Green
	Remove-Item -Path .\htmlcov -Recurse -Force
}

if (Test-Path .\coverage.xml) {
	Write-Host "Removing coverage.xml file" -ForegroundColor Green
	Remove-Item -Path .\coverage.xml -Force
}

if (Test-Path .\.coverage) {
	Write-Host "Removing .coverage file" -ForegroundColor Green
	Remove-Item -Path .\.coverage -Force
}

if (Test-Path .\.mypy_cache) {
	Write-Host "Removing .mypy_cache directory" -ForegroundColor Green
	Remove-Item -Path .\.mypy_cache -Recurse -Force
}

if (Test-Path .\md_report.md) {
	Write-Host "Removing md_report.md file" -ForegroundColor Green
	Remove-Item -Path .\md_report.md -Force
}

Write-Host "Removing __pycache__ directories" -ForegroundColor Green
Get-ChildItem -Path . -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force

Write-Host "Removing .pytest_cache directories" -ForegroundColor Green
Get-ChildItem -Path . -Recurse -Directory -Filter .pytest_cache | Remove-Item -Recurse -Force

Write-Host "Removing .promptflow directories" -ForegroundColor Green
Get-ChildItem -Path . -Recurse -Directory -Filter .promptflow | Remove-Item -Recurse -Force

Write-Host "Removing .output directories" -ForegroundColor Green
Get-ChildItem -Path . -Recurse -Directory -Filter .output | Remove-Item -Recurse -Force

Write-Host "Removing .cache directories" -ForegroundColor Green
Get-ChildItem -Path . -Recurse -Directory -Filter .cache | Remove-Item -Recurse -Force

Write-Host "Removing .benchmarks directories" -ForegroundColor Green
Get-ChildItem -Path . -Recurse -Directory -Filter .benchmarks | Remove-Item -Recurse -Force
