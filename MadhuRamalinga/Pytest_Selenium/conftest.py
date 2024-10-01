import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver #used to assign the driver instance (created with webdriver.Chrome()) to the class level for use within test methods that belong to a test class.
    yield
    driver.close()

@pytest.fixture(scope='class')
def get_driver_data(request):
    driver = webdriver.Chrome()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
