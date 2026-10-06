@echo off
REM Brings up the bridge between n8n and the Gemini Runner extension on http://127.0.0.1:8766, in its own
REM minimised window (close that window to stop it). Safe to run twice: if it already answers, it's left alone.
REM Started with PowerShell's Start-Process, not cmd's `start` (see start_opencut.cmd for why).
setlocal
cd /d "%~dp0"

curl -s -o nul --max-time 3 http://127.0.0.1:8766/health && (echo bridge already running& exit /b 0)
echo starting bridge on :8766
powershell -NoProfile -Command "Start-Process cmd -WindowStyle Minimized -WorkingDirectory '%~dp0' -ArgumentList '/c','title Gemini bridge :8766 && tts\.venv\Scripts\python bridge.py'"
for /l %%i in (1,1,15) do (
    curl -s -o nul --max-time 3 http://127.0.0.1:8766/health && (echo bridge ready& exit /b 0)
    %SystemRoot%\System32\timeout.exe /t 1 /nobreak >nul
)
echo bridge did not come up. Check its minimised window.
exit /b 1
