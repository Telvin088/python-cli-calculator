# Calculator CLI App (Python)
A simple command-line calculator built in Python that supports addition, subtraction, multiplication and division in the calculator_logic.py file, designed to be a module.
The module is then imported and used in the main_cli.py file, which is responsible for fetching user input and also displaying output, according to the logic/evaluation done in the module file (calculator_logic.py)

## Features
- Add, subtract, multiply, divide numbers
- Handles invalid inputs (letters instead of numbers)
- Safe divide-by-zero handling
- Clean user interface
- Loop menu with exit option.

## Installation
1. Clone the repository:
   https://github.com/Telvin088/python-cli-calculator.git
2. Navigate to python-cli-calculator:
   cd python-cli-calculator

## Usage
Run the main script:
python main_cli.py

## Current Issues
- exception blocks return None after every operation
- currently doesn't exit the program when user enters invalid input as operation value