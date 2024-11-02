import pytest
import warnings
from calculator.calculation import Calculator
from calculator.commands import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand, ExitCommand

# Create a fixture for the calculator
@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_command_execute_not_implemented():
    """Test that calling execute on the base Command class raises NotImplementedError."""
    command = Command()
    with pytest.raises(NotImplementedError):
        command.execute(1, 2)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_add_command(calculator):
    """Test the add command."""
    add_command = AddCommand()
    result = add_command.execute(3, 4)
    assert result == calculator.add(3, 4)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_subtract_command(calculator):
    """Test the subtract command."""
    subtract_command = SubtractCommand()
    result = subtract_command.execute(10, 4)
    assert result == calculator.subtract(10, 4)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_multiply_command(calculator):
    """Test the multiply command."""
    multiply_command = MultiplyCommand()
    result = multiply_command.execute(3, 5)
    assert result == calculator.multiply(3, 5)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_divide_command(calculator):
    """Test the divide command."""
    divide_command = DivideCommand()
    result = divide_command.execute(10, 2)
    assert result == calculator.divide(10, 2)

    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        divide_command.execute(10, 0)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_menu_command():
    """Test the menu command."""
    command = MenuCommand()
    expected_output = ("Commands: add, subtract, multiply, divide, load, save, clear, exit\n"
                       "For operations, please provide two numeric arguments (ex: add 1 2)")
    assert command.execute() == expected_output


@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_exit_command():
    """Test the exit command."""
    command = ExitCommand()
    result = command.execute()
    assert result == "Exiting the calculator..."
