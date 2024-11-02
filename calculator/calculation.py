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