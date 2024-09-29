import pytest

"""
fixture: fixture is the function which will work as pre-requisite of 
         any test case/test file or test packages.

--- fixture scopes: ---

function scope: function level will apply of all the test cases and execute setup and teardown 
                for each test case. 
module scope : module level scope works with each test file which contains test function.
package scope : package level scope works with each package which contains multiple module
session scope : Session level scope has a top most, session scope code will always executes first
here is structure of priority.

session scope -> package scope -> module scope ->  function scope

class scope
"""


@pytest.fixture(scope='function')
def fun_setup():
    print("\n -- Function code execution started --")
    yield  # tear down section of fixture
    print("\n -- function execution is done --")


@pytest.fixture(scope='module', autouse=True)
def module_setup():
    print("\n -- Module code execution started --")
    yield  # tear down section of fixture
    print("\n -- Module execution is done --")


@pytest.fixture(scope='package', autouse=True)
def package_setup():
    print("\n -- Package code execution started --")
    yield  # tear down section of fixture
    print("\n -- Package execution is done --")


@pytest.fixture(scope='session', autouse=True)
def session_setup():
    print("\n -- session code execution started --")
    yield  # tear down section of fixture
    print("\n -- session execution is done --")


@pytest.mark.smoke
def test_addition_reg(fun_setup):
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 + b1 + c1 == 120


@pytest.mark.smoke
@pytest.mark.sanity
def test_multiplication_reg(fun_setup):
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 * b1 * c1 == 60000


@pytest.mark.sanity
def test_addition_subtraction_reg(fun_setup):
    a1 = 50
    b1 = 40
    c1 = 30
    assert a1 - b1 - c1 == -20


@pytest.mark.smoke
def test_division_reg(fun_setup):
    a1 = 20
    b1 = 4
    assert a1 / b1 == 5
