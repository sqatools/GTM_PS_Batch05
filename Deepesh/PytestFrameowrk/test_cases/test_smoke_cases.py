import pytest
"""
pip install pytest
"""


@pytest.mark.smoke
def test_addition():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 + b1 + c1 == 110


@pytest.mark.smoke
@pytest.mark.sanity
def test_multiplication():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 * b1 * c1 == 60000


@pytest.mark.sanity
def test_addition_subtraction():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 - b1 - c1 == -20


@pytest.mark.regression
def test_division():
    a1 = 20
    b1 = 4
    assert a1 / b1 == 5
