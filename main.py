def calculator(operation, num1, num2):
    """Perform basic arithmetic operations."""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return num1 / num2
    return None  # Return None for invalid operations

def main():
    """Main function to run the calculator app."""
    print("Welcome to the Calculator App!")
    
    valid_commands = {'add', 'subtract', 'multiply', 'divide', 'exit'}

    # REPL to keep running the app until user quits
    while True:
        print("Commands ('add', 'subtract', 'multiply', 'divide', 'exit'): ")
        user_command = input("Enter command: ").strip().lower()

        if user_command == 'exit':
            print("Goodbye")
            break

        if user_command not in valid_commands:
            print("Invalid command. Please enter a valid command.\n")
            continue

        try:
            user_num1 = float(input("Enter first number: "))
            user_num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue

        try:
            result = calculator(user_command, user_num1, user_num2)
            if result is not None:
                print(f"The result: {result}\n")
            else:
                print("Error: Invalid operation.\n")
        except ZeroDivisionError as e:
            print(f"{e}\n")  # Handle division by zero error

if __name__ == "__main__":
    main()
