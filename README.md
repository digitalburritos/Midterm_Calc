# Mid Term Calculator Project

## Overview
The Mid Term Calculator Project uses a Read-Evaluate-Print Loop (REPL) to enable continuous interaction with a calculator. Users can perform basic arithmetic operations, manage calculation history, and extend functionality with plugins.

## Features
- **Arithmetic Operations**: Add, subtract, multiply, and divide two numeric values.
- **Calculation History**: 
  - **Load**: Retrieve past calculations from a CSV file using Pandas.
  - **Save**: Store current calculation history to a CSV file, allowing for easy retrieval.
  - **Clear**: Remove all entries from the current history, managing data effectively.
- **Plugin System**: Dynamically load commands for enhanced functionality.
- **User-Friendly Interface**: Access a menu of commands for easy navigation.

## Logging and Configuration
- **Logging**: A comprehensive logging system captures user actions and errors, configurable via environment variables.
- **Environment Variables**: Managed through a `.env` file for sensitive information like database credentials.

## Design Patterns
- **Facade Pattern**: Simplifies complex operations with a unified interface.
- **Command Pattern**: Structures commands for easy execution and history management.
- **Factory Method and Strategy Patterns**: Enhance code flexibility and scalability.

