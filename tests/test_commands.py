import pytest
from calculator.calculation import Calculator
from calculator.commands import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand, ExitCommand

# Create a fixture for the calculator
@pytest.fixture
def calculator():
    return Calculator()

def test_command_execute_not_implemented():
    command = Command()
    with pytest.raises(NotImplementedError):
        command.execute(1, 2)

def test_add_command(calculator):
    add_command = AddCommand()
    result = add_command.execute(3, 4)
    assert result == calculator.add(3, 4)

def test_subtract_command(calculator):
    subtract_command = SubtractCommand()
    result = subtract_command.execute(10, 4)
    assert result == calculator.subtract(10, 4)

def test_multiply_command(calculator):
    multiply_command = MultiplyCommand()
    result = multiply_command.execute(3, 5)
    assert result == calculator.multiply(3, 5)

def test_divide_command(calculator):
    divide_command = DivideCommand()
    result = divide_command.execute(10, 2)
    assert result == calculator.divide(10, 2)

    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        divide_command.execute(10, 0)

def test_menu_command():
    command = MenuCommand()
    expected_output = "Commands: add, subtract, multiply, divide, menu, exit"
    assert command.execute() == expected_output

def test_exit_command():
    command = ExitCommand()
    # Assuming ExitCommand doesn't return anything
    result = command.execute()
    assert result == "Exiting the calculator..."