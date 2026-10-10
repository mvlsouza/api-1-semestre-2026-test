@echo off
cls
cd /d "%~dp0backend"
call venv\Scripts\activate.bat
cd src
py main.py
pause