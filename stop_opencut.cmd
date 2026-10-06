@echo off
REM Stops what start_opencut.cmd started: whatever listens on 127.0.0.1:3000 (editor) and :3002
REM (controller, with its headless Chromium), process tree and all. Nothing running is not an error.
for /f "tokens=5" %%p in ('netstat -ano ^| findstr /r /c:"127.0.0.1:3000 .*LISTENING" /c:"127.0.0.1:3002 .*LISTENING"') do taskkill /PID %%p /T /F >nul 2>&1
echo OpenCut stopped
exit /b 0
