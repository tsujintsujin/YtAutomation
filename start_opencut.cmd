@echo off
REM Brings up what the yt-render pipeline needs from OpenCut, both on this PC only:
REM   - the patched OpenCut editor (production build) on http://127.0.0.1:3000
REM   - the opencut-controller MCP server, HTTP transport, on http://127.0.0.1:3002/mcp
REM Each runs in its own minimised window; close that window to stop it. Safe to run twice:
REM anything already answering is left alone.
REM If you edit opencut-classic's source, rebuild first: cd opencut-classic\apps\web ^&^& bun run build
REM
REM The windows are started with PowerShell's Start-Process, not cmd's `start`: `start` hands every
REM inheritable handle to the new window, including n8n's Execute Command pipe, so n8n waited until
REM OpenCut was closed. Start-Process hands none.
REM 127.0.0.1, not localhost: localhost resolves to ::1 first and the editor only listens on IPv4.
setlocal
REM Chromium path: the controller's playwright wants headless_shell-1217, which is not installed;
REM chromium-1234 is (same path as the "opencut" MCP entry in ~/.claude.json).
cd /d "%~dp0"

curl -s -o nul --max-time 3 http://127.0.0.1:3000/ && (echo editor already running) || (
    echo starting OpenCut editor on :3000
    powershell -NoProfile -Command "Start-Process cmd -WindowStyle Minimized -WorkingDirectory '%~dp0opencut-classic\apps\web' -ArgumentList '/c','title OpenCut editor :3000 && bun run start -p 3000 -H 127.0.0.1'"
)

curl -s -o nul --max-time 3 http://127.0.0.1:3002/health && (echo controller already running) || (
    echo starting opencut-controller on :3002
    powershell -NoProfile -Command "Start-Process cmd -WindowStyle Minimized -WorkingDirectory '%~dp0opencut-controller' -ArgumentList '/c','title OpenCut controller :3002 && set TRANSPORT_TYPE=http&& set PORT=3002&& set OPENCUT_URL=http://127.0.0.1:3000&& set CHROMIUM_PATH=%LOCALAPPDATA%\ms-playwright\chromium-1234\chrome-win64\chrome.exe&& node dist\index.js'"
)

echo waiting for both to answer...
for /l %%i in (1,1,90) do (
    curl -s -o nul --max-time 3 http://127.0.0.1:3000/projects && curl -s -o nul --max-time 3 http://127.0.0.1:3002/health && (
        echo OpenCut ready: editor http://127.0.0.1:3000  controller http://127.0.0.1:3002/mcp
        exit /b 0
    )
    REM ping, not timeout.exe: timeout needs a console and exits at once under n8n, so the loop never waited
    ping -n 3 127.0.0.1 >nul
)
echo OpenCut did not come up within 3 minutes. Check the two minimised windows.
exit /b 1
