# PowerShell script to rename the Flask template project
# Usage: ./rename-template.ps1 NewProjectName
param(
    [Parameter(Mandatory = $true)]
    [string]$NewName
)

# Replace in README and docs (md, toml, py)
Get-ChildItem -Path . -Recurse -Include *.md,*.toml,*.py -File | ForEach-Object {
    (Get-Content $_.FullName) -replace 'flask-template', $NewName | Set-Content $_.FullName
}

Write-Host "Renamed project to $NewName. Please review and update any remaining references manually."
