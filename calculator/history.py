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
        self.history_df.to_csv(self.history_file_path, index=False)
        return f"History saved to: {self.history_file_path}"

    def clear_history(self):
        """Clear the calculation history."""
        self.history_df = pd.DataFrame(columns=["operation", "values", "result"])
        return "History cleared."
