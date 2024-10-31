from calculator.calculation import Calculator

calculator = Calculator()

class Command:
    """Base command class for calculator commands."""
    def execute(self, *args):
        """Executes the command with given arguments.
        
        This method should be overridden in subclasses.
        """
        raise NotImplementedError

class MenuCommand(Command):
    """Command to display commands."""
    def execute(self):
        return "Commands: add, subtract, multiply, divide, exit"

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
