import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class HistoryManager:
    """Manages the calculation history (Facade Pattern)."""
    
    def __init__(self):
        self.history_file_path = os.getenv("HISTORY_FILE_PATH", "history.csv")
        self.history_df = pd.DataFrame(columns=["operation", "values", "result"])

    def load_history(self):
        """Load history from a CSV file."""
        if os.path.exists(self.history_file_path):
            self.history_df = pd.read_csv(self.history_file_path)
            return "History loaded successfully."
        return "No history file found."

    def save_history(self):
        """Save history to a CSV file."""
        if os.path.exists(self.history_file_path):
            self.history_df.to_csv(self.history_file_path, mode='a', header=False, index=False)  # Append to existing file
        else:
            self.history_df.to_csv(self.history_file_path, index=False)  # Create new file
        return f"History saved to: {self.history_file_path}"

    def clear_history(self):
        """Clear the calculation history, keeping only the headers in the CSV file."""
        # Create an empty DataFrame with the same columns
        empty_df = pd.DataFrame(columns=["operation", "values", "result"])
        
        # Write the empty DataFrame to the CSV file
        empty_df.to_csv(self.history_file_path, index=False)
        
        # Reset the history DataFrame in memory
        self.history_df = empty_df
        
        return "History cleared."

    def add_history(self, operation, values, result):
        """Add a new calculation to history."""
        new_entry = pd.DataFrame({"operation": [operation], "values": [values], "result": [result]})
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)  # Append new entry

