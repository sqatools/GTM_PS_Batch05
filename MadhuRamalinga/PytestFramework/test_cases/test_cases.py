import pytest

env = 'TEST'


#env = 'PROD'

@pytest.mark.smoke
def test_addition():
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 + b1 + c1 == 110


@pytest.mark.smoke
@pytest.mark.sanity
def test_subtraction():
    a1 = 30
    b1 = 40
    c1 = 5
    assert a1 - b1 - c1 == -15


@pytest.mark.sanity
@pytest.mark.skip
def test_multiplication():
    a1 = 5
    b1 = 10
    c1 = 4
    assert a1 * b1 * c1 == 200


@pytest.mark.skipif(env == 'PROD', reason="Feature is not available in Prod env")
@pytest.mark.regression
def test_division():
    a1 = 50
    b1 = 2
    assert a1 / b1 == 25
