#!/bin/bash

# This is a manual script for operating the ATM simulation

# Define the path to the Python ATM simulation script
ATM_SIMULATION_SCRIPT="./atm_simulation/atm_simul_with_logging.py"

# Check if the Python script exists
if [[ ! -f "$ATM_SIMULATION_SCRIPT" ]]; then
    echo "Error: ATM simulation script not found at $ATM_SIMULATION_SCRIPT"
    exit 1
fi
# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 to run the ATM simulation."
    exit 1
fi
# Check if the ATM simulation script is executable
if [[ ! -x "$ATM_SIMULATION_SCRIPT" ]]; then
    echo "Error: ATM simulation script is not executable. Please check the file permissions."
    exit 1
fi
# Check if the ATM simulation script is a Python script
if [[ ! "$ATM_SIMULATION_SCRIPT" == *.py ]]; then
    echo "Error: ATM simulation script is not a Python script. Please provide a valid Python script."
    exit 1
fi
# Check if the ATM simulation script has the correct shebang
if [[ ! $(head -n 1 "$ATM_SIMULATION_SCRIPT") =~ ^#!.*python ]]; then
    echo "Error: ATM simulation script does not have the correct shebang. Please check the script."
    exit 1
fi
# Check if the ATM simulation script has the correct permissions
if [[ ! -r "$ATM_SIMULATION_SCRIPT" ]]; then
    echo "Error: ATM simulation script is not readable. Please check the file permissions."
    exit 1
fi
# Check if the ATM simulation script has the correct encoding
if [[ ! $(file -i "$ATM_SIMULATION_SCRIPT") =~ utf-8 ]]; then
    echo "Error: ATM simulation script does not have the correct encoding. Please check the file."
    exit 1
fi
# Check if the ATM simulation script has the correct dependencies
if ! python3 -c "import logging" &> /dev/null; then
    echo "Error: ATM simulation script has missing dependencies. Please install the required dependencies."
    exit 1
fi
# Check if the ATM simulation script has the correct arguments
if [[ $# -ne 0 ]]; then
    echo "Error: ATM simulation script does not accept any arguments. Please run the script without any arguments."
    exit 1
fi
# Check if the ATM simulation script has the correct environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Error: ATM simulation script is not running in a virtual environment. Please activate the virtual environment."
    exit 1
fi
# Check if the ATM simulation script has the correct Python version
if [[ $(python3 --version) != *"Python 3."* ]]; then
    echo "Error: ATM simulation script is not running with Python 3. Please check the Python version."
    exit 1
fi
# Check if the ATM simulation script has the correct Python path
if [[ $(which python3) != *"/usr/bin/python3"* ]]; then
    echo "Error: ATM simulation script is not running with the correct Python path. Please check the Python path."
    exit 1
fi
# Check if the ATM simulation script has the correct Python interpreter
if [[ $(head -n 1 "$ATM_SIMULATION_SCRIPT") != *"/usr/bin/python3"* ]]; then
    echo "Error: ATM simulation script is not running with the correct Python interpreter. Please check the Python interpreter."
    exit 1
fi
# Run the ATM simulation
echo "Starting the ATM simulation..."
python3 "$ATM_SIMULATION_SCRIPT"
# This is a manual script

