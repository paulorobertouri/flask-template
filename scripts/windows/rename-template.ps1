$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $ScriptDir)

Set-Location $ProjectRoot

if [ -z "$1" ]; then
echo "Usage: $0 <new-name>"
exit 1
fi
NEW_NAME="$1"
find . -type f \( -name '*.md' -o -name '*.toml' -o -name '*.py' \) -exec sed -i "s/flask-template/$NEW_NAME/g" {} +
