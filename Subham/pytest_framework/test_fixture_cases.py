import pytest

env=("TEST")
@pytest.mark.sanity
@pytest.mark.xfail
def test_addition():
    a=10
    b=20
    c=30
    assert (a+b+c) == 60
@pytest.mark.regression
@pytest.mark.skipif(env == 'TEST',reason ='feature not avilable in test env')
def test_subtraction():
    a = 10
    b = 20
    c = 30
    assert (a - b - c) == 20
@pytest.mark.sanity
@pytest.mark.skip
def test_multiplication():
    a = 10
    b = 20
    c = 30
    assert (a*b*c) == 6000

@pytest.mark.regression
@pytest.mark.skip
@pytest.mark.xfail
def test_divison():
    a = 50
    b = 10
    assert (a/b) == 4