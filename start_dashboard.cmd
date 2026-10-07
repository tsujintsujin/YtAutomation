@echo off
REM Opens the YtAutomation dashboard on http://127.0.0.1:8770 in Chrome, and first brings up what it controls:
REM   n8n     :5678  ..\n8n\start_n8n.cmd in its own minimised window "n8n :5678" (not waited for: n8n takes a
REM                  while to load; the dashboard's n8n dot turns green when it's up)
REM   bridge  :8766  start_bridge.cmd (own minimised window; n8n's workflow also starts it if it isn't up)
REM   dashboard :8770 own minimised window "YtAutomation dashboard :8770"
REM Each is left alone if it already answers, so this is safe to run any number of times.
REM "YtAutomation Dashboard.lnk" next to this file runs it (pin that shortcut; Windows can't pin a .cmd).
REM Windows are started with PowerShell's Start-Process, not cmd's `start` (see start_opencut.cmd for why).
setlocal
cd /d "%~dp0"

curl -s -o nul --max-time 3 http://127.0.0.1:5678/healthz && goto bridge
echo starting n8n on :5678
powershell -NoProfile -Command "Start-Process cmd -WindowStyle Minimized -WorkingDirectory '%~dp0..\n8n' -ArgumentList '/c','title n8n :5678 && .\start_n8n.cmd'"

:bridge
call .\start_bridge.cmd

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
