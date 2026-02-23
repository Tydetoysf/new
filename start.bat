@echo off
echo ===================================
echo Sosa Services - Starting Application
echo ===================================

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Navigate to backend directory
cd web\backend

REM Initialize database if it doesn't exist
if not exist "..\instance\users.db" (
    echo Initializing database...
    python database.py
)

REM Start the application
echo Starting Sosa Services...
echo Access the application at: http://localhost:8888
python app.py

pause
