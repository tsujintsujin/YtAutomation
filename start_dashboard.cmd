@echo off
REM Opens the YtAutomation dashboard on http://127.0.0.1:8770. The server runs in its own minimised window
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
powershell -NoProfile -Command "Start-Process 'http://127.0.0.1:8770/'"
exit /b 0
