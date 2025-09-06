# About: This script is used to change the current directory to the root of the project.

$location = Get-Location

if ($location -like "*\scripts\windows") {
	Write-Host "Changing directory to root..." -ForegroundColor DarkGray
	Set-Location ../../
}
