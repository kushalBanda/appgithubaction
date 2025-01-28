from src.math_operation import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(2, 4) == 6

def test_sub():
    assert sub(5, 3) == 2
    assert sub(5, 4) == 1
    assert sub(5, 5) == 0