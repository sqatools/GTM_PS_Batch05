import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.maximize_window()
    driver.implicitly_wait(20)
    #hold value of driver in driver variable  for any class
    request.cls.driver = driver
    yield
    driver.close()
