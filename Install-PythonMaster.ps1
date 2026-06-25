# Python Master Standalone Installer (Windows)
# Roman Urdu & English Support

Write-Host "=========================================" -ForegroundColor Green
Write-Host "      🐍 Python Master Installer 🐍      " -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host "Starting installation..."

# Setup Directories
$SourceDir = Join-Path $PSScriptRoot "PythonMaster"
$InstallDir = Join-Path $env:USERPROFILE "AppData\Local\Programs\PythonMaster"

# Validate Build
if (-not (Test-Path $SourceDir)) {
    Write-Host "[ERROR] Compiled application files not found at: $SourceDir" -ForegroundColor Red
    Write-Host "Please build the app using PyInstaller first." -ForegroundColor Red
    Exit 1
}

# Create Target Directory
if (-not (Test-Path $InstallDir)) {
    Write-Host "Creating installation directory..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
} else {
    Write-Host "Updating existing installation..." -ForegroundColor Cyan
}

# Copying Files
Write-Host "Copying application files (yeh thoda waqt le sakta hai)..." -ForegroundColor Cyan
Copy-Item -Path "$SourceDir\*" -Destination $InstallDir -Recurse -Force

# Create Desktop Shortcut
Write-Host "Creating Desktop shortcut..." -ForegroundColor Cyan
$DesktopPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), "Python Master.lnk")
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($DesktopPath)
$Shortcut.TargetPath = Join-Path $InstallDir "PythonMasterLauncher.exe"
$Shortcut.WorkingDirectory = $InstallDir
$Shortcut.Description = "Python Master learning app in Roman Urdu"
$Shortcut.Save()

# Create Start Menu Shortcut
Write-Host "Creating Start Menu shortcut..." -ForegroundColor Cyan
$StartMenuPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('StartMenu'), "Programs\Python Master.lnk")
$ShortcutStart = $WshShell.CreateShortcut($StartMenuPath)
$ShortcutStart.TargetPath = Join-Path $InstallDir "PythonMasterLauncher.exe"
$ShortcutStart.WorkingDirectory = $InstallDir
$ShortcutStart.Description = "Python Master learning app in Roman Urdu"
$ShortcutStart.Save()

Write-Host ""
Write-Host "=========================================" -ForegroundColor Green
Write-Host " 🎉 PYTHON MASTER IS SUCCESSFULLY INSTALLED! 🎉 " -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host "Installation Path: $InstallDir" -ForegroundColor White
Write-Host "Desktop aur Start Menu shortcuts create kar diye gaye hain." -ForegroundColor White
Write-Host "Application ko auto-launch kiya ja raha hai..." -ForegroundColor Yellow

# Launch App
$LauncherPath = Join-Path $InstallDir "PythonMasterLauncher.exe"
Start-Process -FilePath $LauncherPath -WorkingDirectory $InstallDir

# Wait for Streamlit server to start, then open browser
Write-Host "Browser mein app open ho rahi hai (5 seconds mein)..." -ForegroundColor Yellow
Start-Sleep -Seconds 5
Start-Process "http://localhost:8501"

Write-Host "Done! App browser mein khul gayi hai." -ForegroundColor Green
