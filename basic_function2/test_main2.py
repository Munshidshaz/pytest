from main2 import add,divide
import pytest

def test_add():
    assert add(1,3) == 4 #" 1 + 3 is 4"
    assert add(3,2) == 5 #"3 + 2 is 5"
    assert add(0,1) == 1 #"0 + 1 is 1"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10,0)
    
def test_divide2():
    with pytest.raises(ValueError) as info_error:
        divide(10,0)
    assert "Cannot divide by zero" == str(info_error.value)