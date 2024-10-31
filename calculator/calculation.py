class Calculator:
    """A simple calculator that can add, subtract, multiply, and divide."""

    def add(self, a: float, b: float) -> float:
        """Adds two numbers and returns the result."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtracts the second number from the first and returns the result."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers and returns the result."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divides the first number by the second and returns the result.
        
        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b