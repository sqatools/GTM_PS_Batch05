import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.log = logging.getLogger(__name__)

    def get_element(self, locator):
        try:
            self.log.info(f"finding element with locator: {locator}")
            element = self.wait.until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.log.info(f"element not found: {locator}")
            self.log.info(e)
            self.driver.save_screenshot('./logs/element_not_found.png')
            raise

    def get_elements_list(self, locator):
        elements_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return elements_list

    def click_element(self, locator):
        self.log.info(f"clicking on element: {locator}")
        element = self.get_element(locator)
        element.click()

    def send_text(self, locator, data):
        self.log.info(f"sending text: {data} to element: {locator}")
        element = self.get_element(locator)
        element.clear()
        element.send_keys(data)

    def select_value_from_dropdown(self, locator, select_value):
        self.log.info(f"select: {select_value} value from dropdown: {locator}")
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(select_value)
