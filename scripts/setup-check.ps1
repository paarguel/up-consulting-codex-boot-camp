# Setup check for UP Consulting Codex Boot Camp.
# Run from the repo root:
# .\scripts\setup-check.ps1

$ErrorActionPreference = "Continue"

function Check-Command {
    param(
        [string]$Name,
        [string]$InstallHint
    )

    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) {
        Write-Host "OK: $Name found at $($cmd.Source)" -ForegroundColor Green
        try {
            & $Name --version
        } catch {
            Write-Host "Note: $Name exists, but version check failed." -ForegroundColor Yellow
        }
    } else {
        Write-Host "MISSING: $Name" -ForegroundColor Red
        Write-Host "  Hint: $InstallHint" -ForegroundColor Yellow
    }

    Write-Host ""
}

Write-Host "UP Consulting Codex Boot Camp setup check" -ForegroundColor Cyan
Write-Host ""

Check-Command "git" "Install Git for Windows."
Check-Command "codex" "Install/open Codex using the official OpenAI Codex setup docs."
Check-Command "python" "Optional for the coding addendum: install Python 3.11+ and reopen PowerShell."
Check-Command "gh" "Optional: install GitHub CLI if you want to publish repos from the terminal."

Write-Host "Next step:" -ForegroundColor Cyan
Write-Host "  Open this folder in Codex, then ask Codex to inspect README.md and AGENTS.md."
Write-Host ""
Write-Host "First prompt:"
Write-Host "  Read README.md and AGENTS.md. Explain this repo to me like I am new to AI-assisted knowledge work. Do not edit files yet."
