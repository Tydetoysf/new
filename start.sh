#!/bin/bash

echo "==================================="
echo "Sosa Services - Starting Application"
echo "==================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Navigate to backend directory
cd web/backend

# Initialize database if it doesn't exist
if [ ! -f "../instance/users.db" ]; then
    echo "Initializing database..."
    python database.py
fi

# Start the application
echo "Starting Sosa Services..."
echo "Access the application at: http://localhost:8888"
python app.py
