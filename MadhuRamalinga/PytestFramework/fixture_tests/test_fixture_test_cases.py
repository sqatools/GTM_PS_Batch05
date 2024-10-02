import pytest


@pytest.fixture(scope='function')
def func_setup():
    print("---Function code execution started---")
    yield
    print("---Function execution completed---")


@pytest.fixture(scope='module', autouse=True)
def module_setup():
    print("---Module code execution started---")
    yield
    print("---Module execution completed---")

@pytest.fixture(scope='package', autouse=True)
def pkg_setup():
    print("---Package code execution started---")
    yield
    print("---Package execution completed---")

@pytest.fixture(scope='session', autouse=True)
def session_setup():
    print("---Session code execution started---")
    yield
    print("---Session execution completed---")

@pytest.mark.smoke
def test_addition(func_setup):
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 + b1 + c1 == 120


@pytest.mark.smoke
@pytest.mark.sanity
def test_subtraction(func_setup):
    a1 = 30
    b1 = 40
    c1 = 5
    assert a1 - b1 - c1 == -15


@pytest.mark.sanity
def test_multiplication(func_setup):
    a1 = 5
    b1 = 10
    c1 = 4
    assert a1 * b1 * c1 == 200


@pytest.mark.smoke
def test_division(func_setup):
    a1 = 50
    b1 = 2
    assert a1 / b1 == 25

#command: python -m pytest -v -s .\test_fixture_test_cases.py
