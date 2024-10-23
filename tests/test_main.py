import pytest
from main import calculator

def test_add():
    assert calculator('add', 2, 3) == 5
    assert calculator('add', -1, 1) == 0
    assert calculator('add', 0, 0) == 0

def test_subtract():
    assert calculator('subtract', 5, 3) == 2
    assert calculator('subtract', 3, 5) == -2
    assert calculator('subtract', 0, 0) == 0

def test_multiply():
    assert calculator('multiply', 2, 3) == 6
    assert calculator('multiply', -1, 1) == -1
    assert calculator('multiply', 0, 10) == 0

def test_divide():
    assert calculator('divide', 6, 3) == 2
    assert calculator('divide', -6, 3) == -2
    assert calculator('divide', 0, 1) == 0

    with pytest.raises(ZeroDivisionError):
        calculator('divide', 1, 0)

def test_invalid_operation():
    assert calculator('invalid_op', 1, 1) is None