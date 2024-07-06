#!/bin/bash

# Function to deactivate virtual environment and run the application
run_app() {
    # Run the main application
    if [ ! -f "main.py" ]; then
        echo "main.py not found!"
        exit 1
    fi

    python main.py
    if [ $? -ne 0 ]; then
        echo "Failed to run the main application."
        exit 1
    fi

    # Deactivate virtual environment
    deactivate
    if [ $? -ne 0 ]; then
        echo "Failed to deactivate virtual environment."
        exit 1
    fi
}

run_app
