import sys
import logging
import logging.config
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand, ExitCommand
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():
    commands = {
        "add": AddCommand(),
        "subtract": SubtractCommand(),
        "multiply": MultiplyCommand(),
        "divide": DivideCommand(),
        "menu": MenuCommand(),
        "exit": ExitCommand(),
    }

    logger.info("Calculator started.")
    print("*\nWelcome to the Calculator!")
  
    """Main REPL loop for the interactive calculator."""
    while True:
        print()
        query = input("Type \"menu\" for commands or \"exit\" to exit program': ").lower().strip()
        print()

        if query == "menu":
            print(commands[query].execute(), end = "\n")
            logger.info("Menu commands accessed")
            print()

        elif query == "exit":
            print(commands[query].execute())
            logger.info("Calculator exited.")
            break
        else:
            print("Try typing the commands again.\n")
            logger.warning("Commands input wrong")
            continue

        user_input = input("Enter command with arguments(ex: add 1 2): ").strip()
        parts = user_input.split()
        command_name = parts[0] if parts else ""
        
        """LBYL to check if the command is valid before executing."""
        if command_name in commands:
            try:
                """Attempt to convert arguments to float"""
                args = list(map(float, parts[1:])) if len(parts) > 1 else []
            except ValueError:
                print("Error: Please provide numeric arguments after the command.\n")
                logger.error(f"Invalid arguments for command '{command_name}': {parts[1:]}")
                continue
            
            """Check for command-specific argument requirements."""
            if command_name in ["add", "subtract", "multiply", "divide"] and len(args) < 2:
                print("This command requires two numeric arguments.")
                logger.warning(f"{command_name} command requires two numeric arguments.")
            else:
                """EAFP to attempt the calculation and raise relevent errors as needed"""
                try:
                    result = commands[command_name].execute(*args)
                    print(f"Result: {result}\n")
                    logger.info(f"Executed command: {command_name} with args: {args}, result: {result}")
                except (ValueError, ZeroDivisionError) as e:
                    print(f"Error: {e}\n")
                    logger.error(f"{type(e).__name__}: {str(e)}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}\n")
                    logger.error(f"Unexpected error: {e}")
        else:
            print("Unknown command.")
            logger.warning(f"Unknown command: {command_name}")

if __name__ == "__main__":
    main()