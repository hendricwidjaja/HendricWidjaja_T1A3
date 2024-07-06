#!/bin/bash

# Check if Python3 is installed
if command -v python3 &>/dev/null; then
    echo "Python3 is installed"
    python3 --version
else
    echo "You don't have Python3 installed. Please install Python3 and try again."
    exit 1
fi
