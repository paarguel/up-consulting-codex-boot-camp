# Create and publish this boot camp repo to GitHub.
# Requires GitHub CLI: https://cli.github.com/
#
# Run from the root of up-consulting-codex-boot-camp:
# .\scripts\create-public-github-repo.ps1

$ErrorActionPreference = "Stop"

$RepoName = "up-consulting-codex-boot-camp"
$Description = "Beginner-friendly Codex boot camp materials, prompts, and exercises from UP Consulting."

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "GitHub CLI 'gh' is not installed. Install it first, then run this script again."
}

if (-not (Test-Path ".git")) {
    git init
}

git add .

git rev-parse --verify HEAD *> $null
if ($LASTEXITCODE -ne 0) {
    git commit -m "Initial Codex boot camp materials"
} elseif (-not [string]::IsNullOrWhiteSpace((git status --porcelain))) {
    git add .
    git commit -m "Update Codex boot camp materials"
}

gh repo create $RepoName --public --description $Description --source . --remote origin --push

Write-Host "Published GitHub repo: $RepoName" -ForegroundColor Green
