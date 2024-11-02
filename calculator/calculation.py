import pandas as pd
import os
import logging
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Calculator:
    """Basic calculator for performing operations."""
    
    def __init__(self):
        self.history_df = pd.DataFrame(columns=["operation", "values", "result"])
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract second number from first."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide first number by second."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")  # EAFP: Handle exception for division by zero
        return a / b

    def add_to_history(self, operation, values, result):
        """Add a new calculation to history."""
        new_entry = pd.DataFrame({"operation": [operation], "values": [values], "result": [result]})
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)  # Store calculations
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history_df = pd.DataFrame(columns=["operation", "values", "result"])
        return "History cleared."
   
    def load_history(self, file_path):
        """Load history from a CSV file."""
        if os.path.exists(file_path):
            self.history_df = pd.read_csv(file_path)
            return "History loaded successfully."
        return "No history file found."