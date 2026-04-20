@echo off
echo 🚀 Starting DSO138mini Web Plotter...
echo.

python server.py
if errorlevel 1 (
    echo.
    echo ❌ Error: Python not found!
    echo Make sure Python 3 is installed and in PATH
    echo.
    pause
)
