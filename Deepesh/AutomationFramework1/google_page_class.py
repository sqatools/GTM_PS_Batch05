from selenium_base import SeleniumBase
from google_page_class_data import *


class GooglePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def open_google_page(self, url):
        self.driver.get(url)

    def enter_value_to_search_box(self, search_data):
        self.send_text(google_search_box_locator, search_data)

    def click_to_search_button(self):
        self.click_element(search_button_locator)
