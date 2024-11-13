import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://flights.booking.com/")
    request.cls.driver = driver
    yield
    driver.close()


