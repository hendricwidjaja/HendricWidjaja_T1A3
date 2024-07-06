#!/bin/bash

# Run check_python.sh to check if python3 is installed
./check_python.sh
if [ $? -ne 0 ]; then
    echo "check_python.sh failed."
    exit 1
fi

# Run setup.sh to setup virtual environment and install dependencies
./setup.sh
if [ $? -ne 0 ]; then
    echo "setup.sh failed."
    exit 1
fi

# Run run_app.sh to run main application
./run_app.sh
if [ $? -ne 0 ]; then
    echo "run_app.sh failed."
    deactivate
    exit 1
fi

echo "All scripts executed successfully."
