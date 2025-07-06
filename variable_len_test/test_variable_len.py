import pytest
from variable_len import prime_finder

@pytest.mark.parametrize("num, expected",[
    (1,False),
    (2,True),
    (3,True),
    (4,False),
    (5,True),
    (6,False),
    (17,True),
    (25,False)

])

def test_prime_finder(num, expected):
    assert prime_finder(num) == expected
    