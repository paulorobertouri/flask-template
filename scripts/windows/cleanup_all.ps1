# About: This script is used to clean up a virtual environment.

function Remove-Items($directories) {
    foreach ($directory in $directories) {
        Write-Host "Removing $directory directories" -ForegroundColor Green
        Get-ChildItem -Path . -Recurse -Directory -Filter $directory | Remove-Item -Recurse -Force
    }
}

function Remove-Files($files) {
    foreach ($file in $files) {
        Write-Host "Removing $file files" -ForegroundColor Green
        Get-ChildItem -Path . -Recurse -File -Filter $file | Remove-Item -Force
    }
}

$directoriesToRemove = @(
    "bin",
    "build",
    "dist",
    # Python build directories
    "htmlcov",
    ".mypy_cache",
    "__pycache__",
    ".pytest_cache",
    ".promptflow",
    # Temporary directories
    ".benchmarks",
    ".cache",
    ".output",
    ".dump",
    ".data",
    ".test",
    # Python virtual environments
    ".py-venv",
    ".venv",
    # Node.js virtual environments
    "node_modules",
    ".next"
)

$filesToRemove = @(
    "coverage.xml",
    ".coverage",
    "md_report.md"
)

Remove-Items $directoriesToRemove

Remove-Files $filesToRemove

Write-Host "Cleaning up npm cache" -ForegroundColor Green

npm cache clean --force

Write-Host "Cleaning up pip cache" -ForegroundColor Green

pip cache purge

Write-Host "Cleaning up docker containers" -ForegroundColor Green

docker system prune -a --volumes -y

Write-Host "Done cleaning up" -ForegroundColor Green
