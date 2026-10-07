@echo off
REM Opens the YtAutomation dashboard on http://127.0.0.1:8770 in Chrome. "YtAutomation Dashboard.lnk" next to this
REM file runs it (pin that shortcut to the taskbar; Windows can't pin a .cmd). The server runs in its own minimised window
REM "YtAutomation dashboard :8770" (close that window to stop it). Safe to run twice: if it already answers, it's
REM left alone. Started with PowerShell's Start-Process, not cmd's `start` (see start_opencut.cmd for why).
setlocal
cd /d "%~dp0"

curl -s -o nul --max-time 3 http://127.0.0.1:8770/ && goto open
echo starting dashboard on :8770
powershell -NoProfile -Command "Start-Process cmd -WindowStyle Minimized -WorkingDirectory '%~dp0' -ArgumentList '/c','title YtAutomation dashboard :8770 && tts\.venv\Scripts\python dashboard.py'"
for /l %%i in (1,1,15) do (
    curl -s -o nul --max-time 3 http://127.0.0.1:8770/ && goto open
    %SystemRoot%\System32\timeout.exe /t 1 /nobreak >nul
)
echo dashboard did not come up. Check its minimised window.
exit /b 1

:open
REM Chrome, not the default browser (Edge on this PC); the default only if Chrome isn't installed
set "CHROME=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if exist "%CHROME%" (
    powershell -NoProfile -Command "Start-Process -FilePath $env:CHROME -ArgumentList 'http://127.0.0.1:8770/'"
) else (
    powershell -NoProfile -Command "Start-Process 'http://127.0.0.1:8770/'"
)
exit /b 0
