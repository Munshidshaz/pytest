from re import M, sub
from signal import valid_signals
from _pytest.compat import safe_isclass
import pytest
from simple_calculator import *

def test_add():
    assert add(1,2) == 3
    assert add(-1,1) == 0
    assert add(-2,1) == -1
    assert add(0.5,0.5) == 1.0

def test_subtract():
    assert subtract(2,1) == 1
    assert subtract(1,2) == -1
    assert subtract(0,2) == -2
    assert subtract(-1,-2) == 1

def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(0,2) == 0
    assert multiply(-1,3) == -3
    assert multiply('*',3) == '***'

def test_divide():
    assert divide(2,1) == 2
    assert divide(4,2) == 2
    assert divide(-10,2) == -5
    assert divide(5,2) == 2.5
    with pytest.raises(ValueError,match='Cannot divide by zero'):
        divide(2,0)

def test_is_even():
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(-4) == True
    assert is_even(-5) == False

def test_factorial():
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
    with pytest.raises(ValueError,match="Factorial is not defined for negative numbers"):
            assert factorial(-10)
