import pytest
@pytest.mark.smoke
@pytest.mark.regression
def test_addition():
    a1= 50
    b1 = 40
    c1 = 30
    assert a1 +b1 +c1 == 110

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_multiplication():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 * b1 * c1 ==6000
@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_substraction():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 - b1 - c1 ==-20