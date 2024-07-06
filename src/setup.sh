#!/bin/bash

# Function to create virtual environment and install dependencies
setup() {
    # Check if requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        echo "requirements.txt could not be found. Exiting..."
        exit 1
    fi

    # Create virtual environment
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Virtual Environment could not be created. Exiting..."
        exit 1
    fi

    # Activate virtual environment
    source venv/bin/activate
    if [ $? -ne 0 ]; then
        echo "Virtual Environment could not be activated. Exiting..."
        exit 1
    fi

    # Attempt to upgrade pip
    pip install --upgrade pip
    if [ $? -ne 0 ]; then
        echo "Pip could not be upgraded. Continuing with current version of pip... "
    fi

    # Install dependencies
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Dependencies failed to install. Exiting..."
        deactivate
        exit 1
    fi

    echo "Virtual environment & dependencies setup successfully."
}

setup
