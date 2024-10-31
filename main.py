import sys
import logging
import logging.config
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
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
    }

    logger.info("Calculator started.")

    """Main REPL loop for the interactive calculator."""
    while True:

        print("*\nWelcome to the Calculator!")
        print("Commands: add <num1> <num2>, subtract <num1> <num2>, multiply <num1> <num2>, divide <num1> <num2>")
         
        """EAFP to try the input's execution to raise errors if needed"""
        try:
           
            user_input = input("Enter command (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                logger.info("Calculator exited.")
                break

            parts = user_input.split()
            command_name = parts[0]
            args = list(map(float, parts[1:]))

            """LBYL to check if the command is valid"""
            if command_name in commands:
                result = commands[command_name].execute(*args)
                print(f"Result: {result}")
                logger.info(f"Executed command: {command_name} with args: {args}, result: {result}")
            else:
                print("Unknown command.")
                logger.warning(f"Unknown command: {command_name}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            logger.error("ValueError: Invalid input.")
        except ZeroDivisionError as e:
            print(e)
            logger.error("ZeroDivisionError: Division by zero attempted.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logger.error(f"Unexpected error: {e}")
        
        print()

if __name__ == "__main__":
    main()