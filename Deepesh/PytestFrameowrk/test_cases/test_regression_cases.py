import pytest


@pytest.mark.smoke
def test_addition_reg():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 + b1 + c1 == 110


@pytest.mark.smoke
@pytest.mark.sanity
def test_multiplication_reg():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 * b1 * c1 == 60000


@pytest.mark.sanity
def test_addition_subtraction_reg():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 - b1 - c1 == -20


@pytest.mark.regression
def test_division_reg():
    a1 = 20
    b1 = 4
    assert a1 / b1 == 5
