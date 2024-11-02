# Mid Term Calculator Project
Video Demostration: https://www.flexclip.com/share/72421159c5b1b659847994f509f6d5d0bd7e749.html

## Overview
This Mid Term Calculator Project is a command-line calculator that uses a Read-Evaluate-Print Loop (REPL) for user interaction. It supports basic arithmetic operations and manages calculation history efficiently.

## Table of Contents
- Features
- Setup Instructions
- Usage Examples
- Architectural Decisions
- Design Patterns
- Logging Strategy

## Features
- Arithmetic Operations: Perform addition, subtraction, multiplication, and division on two numeric values.
- Calculation History: 
  -- Load: Retrieve past calculations from a CSV file using Pandas.
  -- Save: Store current calculation history to a CSV file.
  -- Clear: Remove all entries from the current history.
- Plugin System: Dynamically load commands for enhanced functionality.
- User-Friendly Interface: Access a menu of commands for easy navigation.

## Setup Instructions
1. Clone the Repository:
git clone https://github.com/yourusername/Midterm_Calc.git cd Midterm_Calc

2. Create a Virtual Environment (optional but recommended):
python3 -m venv my_env source my_env/bin/activate # On Windows use my_env\Scripts\activate

3. Install Required Packages:
pip install -r requirements.txt

4. Configure Environment Variables: Create a `.env` file in the root directory:
ENVIRONMENT=DEVELOPMENT DATABASE_USERNAME=root HISTORY_FILE_PATH=history.csv

5. Run the Application:
python main.py

## Usage Examples
- Accessing Commands:
- View available commands: `menu`

- Basic Operations:
- To add two numbers: `add 1 2`
- To subtract: `subtract 5 3`
- To multiply: `multiply 4 2`
- To divide: `divide 8 4`

- Managing History:
- Save history: `save`
- Load history: `load`
- Clear history: `clear`

## Architectural Decisions

### Design Patterns and Concepts
- Facade Pattern: Provides a simplified interface for complex data operations involving Pandas. For implementation details, see [Facade Pattern in Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/history.py#L7-L27).

- Command Pattern: Encapsulates each command (add, subtract, etc.) as an object for easier management and extension. See [Command Pattern in Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/main.py#L10-L21).

- Factory Method: Used for creating command instances dynamically. Details can be found in [Factory Method Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/commands.py#L5-L84).

- Singleton Pattern: Ensures the history manager is instantiated only once. See [Singleton Pattern Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/main.py#L10-L11).

- Strategy Pattern: Allows swapping different calculation strategies with the use of plugins and class instantiation. Refer to [Strategy Pattern Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/commands.py#L22-L25).

- **REPL (Read-Eval-Print Loop)**: Facilitates direct interaction with the calculator, allowing users to enter commands and receive immediate feedback. Refer to [REPL Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/main.py#L26-L59).

- **LBYL (Look Before You Leap)**: Checks user input for validity before executing commands to prevent errors. This ensures that only valid commands are processed. Refer to [LBYL Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/main.py#L29-L34).

- **EAFP (Easier to Ask for Forgiveness than Permission)**: Attempts calculations and handles exceptions as they arise, allowing for cleaner and more efficient code. This approach is particularly useful for managing invalid inputs and division errors. Refer to [EAFP Code](https://github.com/digitalburritos/Midterm_Calc/blob/main//main.py#L45-L54).

- **Environment Variables**: Utilizes environment variables to manage sensitive information and configuration settings, such as file paths and database credentials. This is achieved through a `.env` file and the `dotenv` library. Refer to [Environment Variables Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/calculation.py#L4-L6).


### Logging Strategy
The logging system captures user actions and errors at various severity levels (INFO, WARNING, ERROR).

- Configuration: Configured through `logging.conf` for flexible management. See [Logging Configuration Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/logging.conf#L1-L28).

- Usage in Code: Logger methods record events such as command execution and errors. Example usage can be seen in [Logging Usage Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/main.py#L52-L54).


