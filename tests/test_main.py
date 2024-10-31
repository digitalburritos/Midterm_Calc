import pytest
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    """Tests the AddCommand execution."""
    command = AddCommand()
    assert command.execute(3, 4) == 7

def test_subtract_command():
    """Tests the SubtractCommand execution."""
    command = SubtractCommand()
    assert command.execute(10, 5) == 5

def test_multiply_command():
    """Tests the MultiplyCommand execution."""
    command = MultiplyCommand()
    assert command.execute(3, 4) == 12

def test_divide_command():
    """Tests the DivideCommand execution."""
    command = DivideCommand()
    assert command.execute(10, 2) == 5

def test_divide_by_zero_command():
    """Tests DivideCommand execution with zero to ensure it raises an exception."""
    command = DivideCommand()
    with pytest.raises(ZeroDivisionError):
        command.execute(10, 0)