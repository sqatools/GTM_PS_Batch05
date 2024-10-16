import time

import pytest
from base.selenium_base_class import SeleniumBase
from .makemytrip_website_locator import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class MakeMyTripWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def create_new_account(self):
        self.click_element(create_new_acc)

    def dropdown_element(self):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(country_code_dd))
        country_code = self.get_element(country_code_dd)
        action.move_to_element(country_code).click().perform()

        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(select_country_code))
        select_cc = self.get_element(select_country_code)
        action.move_to_element(select_cc).click().perform()

    '''def select_country_code(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(select_country_code))
        self.click_element(select_country_code)'''

    def create_acc_with_ph_no(self, enter_ph_no):
        self.send_text(sign_up_with_phno, enter_ph_no)
        self.click_element(continue_button1)
        time.sleep(30)
        self.click_element(verify_and_create_acc)


