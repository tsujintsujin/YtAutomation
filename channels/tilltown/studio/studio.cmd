@echo off
rem Runs any studio command with the studio's own Chromium (on D:, not C:) and Python venv.
rem   studio.cmd node render.mjs --project projects\<slug> --sheet --scale 0.5
rem   studio.cmd python tools\doctor.py
set "PLAYWRIGHT_BROWSERS_PATH=%~dp0.browsers"
set "PATH=%~dp0.venv\Scripts;%PATH%"
cd /d "%~dp0"
%*
