#!/bin/bash

# Run check_python.sh to check if python3 is installed
./check_python.sh
if [ $? -ne 0 ]; then
    echo "Executable: check_python.sh failed. Exiting..."
    exit 1
fi

# Run setup.sh to setup virtual environment and install dependencies
./setup.sh
if [ $? -ne 0 ]; then
    echo "Executable: setup.sh failed. Exiting..."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Virtual Environment could not be activated. Exiting..."
    exit 1
fi

# Run run_app.sh to run main application
./run_app.sh
if [ $? -ne 0 ]; then
    echo "run_app.sh failed."
    deactivate
    exit 1
fi

# Deactivate virtual environment
deactivate
if [ $? -ne 0 ]; then
    echo "Failed to deactivate virtual environment."
    exit 1
fi

echo "All scripts executed successfully."
