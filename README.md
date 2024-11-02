# Mid Term Calculator Project

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
  - Load: Retrieve past calculations from a CSV file using Pandas.
  - Save: Store current calculation history to a CSV file.
  - Clear: Remove all entries from the current history.
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

### Design Patterns
- Facade Pattern: Provides a simplified interface for complex data operations involving Pandas. For implementation details, see [Facade Pattern in Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/history.py#L7-L29).

- Command Pattern: Encapsulates each command (add, subtract, etc.) as an object for easier management and extension. See [Command Pattern in Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/main.py#L10-L21).

- Factory Method: Used for creating command instances dynamically. Details can be found in [Factory Method Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/commands.py#L4-L65).

- Singleton Pattern: Ensures the logger is instantiated only once. See [Singleton Pattern Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/facade.py#L10-L11).

- Strategy Pattern: Allows swapping different calculation strategies. Refer to [Strategy Pattern Code](https://github.com/digitalburritos/Midterm_Calc/blob/main/calculator/facade.py#L23-L26).

### Logging Strategy
The logging system captures user actions and errors at various severity levels (INFO, WARNING, ERROR).

- Configuration: Configured through `logging.conf` for flexible management.

- Usage in Code: Logger methods record events such as command execution and errors.

