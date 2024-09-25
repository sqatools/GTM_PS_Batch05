import pytest

@pytest.mark.smoke
def test_addition():
    a1=10
    b1=20
    c1=30
    assert (a1+b1+c1)==60

@pytest.mark.smoke
def test_subtraction():
    a1 = 40
    b1 = 20
    c1 = 10
    assert (a1/b1/c1) == 10

@pytest.mark.sanity
def test_multiplication():
    a1 = 10
    b1 = 20
    c1 = 30
    assert (a1 * b1 * c1) == 6000

