import pytest

env=("TEST")


@pytest.fixture(scope='function')
def fun_setup():
    print("\n -- Module code execution started --")
    yield  # tear down section fixture
    print("\n -- Module execution is done --")


@pytest.mark.sanity
@pytest.mark.xfail
def test_addition(fun_setup):
    a=10
    b=20
    c=30
    assert (a+b+c) == 60
@pytest.mark.regression
#@pytest.mark.skipif(env == 'TEST',reason ='feature not avilable in test env')
def test_subtraction(fun_setup):
    a = 10
    b = 20
    c = 30
    assert (a - b - c) == 20
@pytest.mark.sanity
#@pytest.mark.skip
def test_multiplication(fun_setup):
    a = 10
    b = 20
    c = 30
    assert (a*b*c) == 6000

@pytest.mark.regression
#@pytest.mark.skip
@pytest.mark.xfail
def test_divison(fun_setup):
    a = 50
    b = 10
    assert (a/b) == 4