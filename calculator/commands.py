from calculator.calculation import Calculator
import pandas as pd
import os

calculator = Calculator()

HISTORY_FILE = "history.csv"

class Command:
    """Base command class for calculator commands."""
    def execute(self, *args):
        """Executes the command with given arguments.
        
        This method should be overridden in subclasses.
        """
        raise NotImplementedError

class MenuCommand(Command):
    """Command to display available commands."""
    def execute(self):
        return (
            "Available commands:\n"
            "- add: Add two numbers (ex: add 1 2)\n"
            "- subtract: Subtract second number from first (ex: subtract 5 3)\n"
            "- multiply: Multiply two numbers (ex: multiply 2 3)\n"
            "- divide: Divide first number by second (ex: divide 6 2)\n"
            "- load history: Load calculation history from file\n"
            "- save history: Save current history to file\n"
            "- clear history: Clear the calculation history\n"
            "- exit: Exit the program\n"
        )
    
class ExitCommand(Command):
    """Command to exit the calculator."""
    def execute(self):
        return "Exiting the calculator..."

class AddCommand(Command):
    """Command to add two numbers."""
    def execute(self, a, b):
        return calculator.add(a, b)

class SubtractCommand(Command):
    """Command to subtract one number from another."""
    def execute(self, a, b):
        return calculator.subtract(a, b)

class MultiplyCommand(Command):
    """Command to multiply two numbers."""
    def execute(self, a, b):
        return calculator.multiply(a, b)

class DivideCommand(Command):
    """Command to divide one number by another."""
    def execute(self, a, b):
        return calculator.divide(a, b)

class HistoryCommand(Command):
    """Command to manage calculation history."""
    def __init__(self):
        self.history_df = self.load_history()

    def load_history(self):
        """Load history from a CSV file into a DataFrame."""
        if os.path.exists(HISTORY_FILE):
            return pd.read_csv(HISTORY_FILE)
        return pd.DataFrame(columns=["operation", "values", "result"])

    def save_history(self):
        """Save the history DataFrame to a CSV file."""
        self.history_df.to_csv(HISTORY_FILE, index=False)

    def clear_history(self):
        """Clear the history CSV file."""
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
            self.history_df = pd.DataFrame(columns=["operation", "values", "result"])
            return "History cleared."
        return "No history to clear."