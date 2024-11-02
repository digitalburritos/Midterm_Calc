import pandas as pd
import os
from calculator.calculation import Calculator

class Command:
    """Base command class for calculator commands (Command Pattern)."""
    def execute(self, *args):
        """Executes the command with given arguments."""
        raise NotImplementedError

class MenuCommand(Command):
    """Command to display available commands."""
    def execute(self):
        return ("Commands: add, subtract, multiply, divide, load, save, clear, exit\n"
                "For operations, please provide two numeric arguments (ex: add 1 2)")

class ExitCommand(Command):
    """Command to exit the calculator."""
    def execute(self):
        return "Exiting the calculator..."

class AddCommand(Command):
    """Command to add two numbers."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a, b):
        result = Calculator().add(a, b)
        self.history_manager.add_history("add", f"{a}, {b}", result)  # Add to history
        return result

class SubtractCommand(Command):
    """Command to subtract one number from another."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a, b):
        result = Calculator().subtract(a, b)
        self.history_manager.add_history("subtract", f"{a}, {b}", result)  # Add to history
        return result

class MultiplyCommand(Command):
    """Command to multiply two numbers."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a, b):
        result = Calculator().multiply(a, b)
        self.history_manager.add_history("multiply", f"{a}, {b}", result)  # Add to history
        return result

class DivideCommand(Command):
    """Command to divide one number by another."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a, b):
        result = Calculator().divide(a, b)
        self.history_manager.add_history("divide", f"{a}, {b}", result)  # Add to history
        return result

class LoadHistoryCommand(Command):
    """Command to load calculation history."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self):
        return self.history_manager.load_history()

class SaveHistoryCommand(Command):
    """Command to save calculation history."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self):
        return self.history_manager.save_history()

class ClearHistoryCommand(Command):
    """Command to clear the calculation history."""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self):
        return self.history_manager.clear_history()

