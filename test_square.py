import pytest
from square import cal_square

def test_square1():
    assert cal_square(2) == 4
    assert cal_square(-3) == 9
    assert cal_square(0) == 0
    assert cal_square(1.5) == 2.25
    assert cal_square(-1.5) == 2.25
                
