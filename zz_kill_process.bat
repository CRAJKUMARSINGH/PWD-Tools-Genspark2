@echo off
title PWD Tools Hub - Kill Processes
echo ========================================
echo   PWD Tools Hub - Kill Running Processes
echo ========================================
echo.

echo Killing any running PWD Tools Hub processes...
echo.

REM Kill any Python processes running Streamlit apps
taskkill /f /im python.exe /fi "WINDOWTITLE eq PWD Tools Hub*" >nul 2>&1

REM Kill any Streamlit processes specifically
taskkill /f /im streamlit.exe >nul 2>&1

REM Kill processes on common Streamlit ports
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8501') do (
    taskkill /f /pid %%a >nul 2>&1
)

for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8502') do (
    taskkill /f /pid %%a >nul 2>&1
)

for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8503') do (
    taskkill /f /pid %%a >nul 2>&1
)

echo Processes terminated.
echo.
echo All PWD Tools Hub related processes have been stopped.
echo.

pause