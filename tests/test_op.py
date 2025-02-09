from ops import *
def test_add():
    res = add(3,4)
    assert res == 7

def test_sub():
    res = sub(3, 4)
    assert res == -1

def test_multply():
    res = multply(3, 4)
    assert res == 12

def test_division():
    res = division(2, 4)
    assert res == 0.5