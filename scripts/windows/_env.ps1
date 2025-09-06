# About: This script contains functions to work with environment variables

function GetKeyFromEnvFile($key, $envFile = ".env") {
	$envFile = Resolve-Path $envFile
	$env = Get-Content $envFile | ForEach-Object {
		if ($_ -match "^$key=(.*)") {
			$matches[1]
		}
	}
	return $env
}
