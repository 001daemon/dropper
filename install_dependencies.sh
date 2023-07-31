#!/bin/bash

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git before proceeding."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python before proceeding."
    exit 1
fi

# List the required Python packages here
required_packages=("pynput" "other_dependency")

# Function to check if a Python package is installed
is_package_installed() {
    python -c "import $1" &> /dev/null
}

# Install missing Python packages
for package in "${required_packages[@]}"; do
    if ! is_package_installed "$package"; then
        echo "Installing $package..."
        pip install "$package"
    fi
done

echo "All prerequisites are installed."
