import logging
from calculator.commands import (
    AddCommand, SubtractCommand, MultiplyCommand, DivideCommand,
    LoadHistoryCommand, SaveHistoryCommand, ClearHistoryCommand, MenuCommand, ExitCommand
)
from calculator.history import HistoryManager

def main():
    """Main entry point for the REPL (Read-Eval-Print Loop)."""
    history_manager = HistoryManager()  # Create history manager
    commands = {
        "add": AddCommand(history_manager),
        "subtract": SubtractCommand(history_manager),
        "multiply": MultiplyCommand(history_manager),
        "divide": DivideCommand(history_manager),
        "load": LoadHistoryCommand(history_manager),
        "save": SaveHistoryCommand(history_manager),
        "clear": ClearHistoryCommand(history_manager),
        "menu": MenuCommand(),
        "exit": ExitCommand(),
    }


    print("Type 'menu' for commands or 'exit' to exit the program.")

    while True:
        query = input("Enter command: ").strip().lower()
        
        if query == "exit":
            print(commands["exit"].execute())
            break
        elif query == "menu":
            print(commands["menu"].execute())
            continue

        parts = query.split()
        command_name = parts[0]
        args = parts[1:]

        if command_name in commands:
            if command_name in ["add", "subtract", "multiply", "divide"]:
                if len(args) != 2:
                    print("This command requires two numeric arguments.")  # LBYL: Check argument count before processing
                    continue
                try:
                    a, b = map(float, args)
                    result = commands[command_name].execute(a, b)
                    print(f"Result: {result}")
                    logging.info("SUCCESS")
                except ValueError:
                    print("Please enter valid numbers.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    logging.error("ERROR")
            else:
                print(commands[command_name].execute())
        else:
            print("Unknown command. Type 'menu' for available commands.")
            logging.warning(f"UNKNOWN COMMAND: {query}")

if __name__ == "__main__":
    main()