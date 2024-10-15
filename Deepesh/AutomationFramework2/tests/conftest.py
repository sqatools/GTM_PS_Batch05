import pytest
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
from selenium import webdriver
from base.webdriver_factory import WebdriverFactory
from ..session_data import *


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default=None, help='browser to launch')
    parser.addoption("--headless", action='store', default=None, help='GUI execution option')


@pytest.fixture(scope='class')
def get_driver_with_option(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless = pytestconfig.getoption("headless")
    wf = WebdriverFactory(browser=browser, headless=headless)
    driver = wf.get_driver_instance()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
