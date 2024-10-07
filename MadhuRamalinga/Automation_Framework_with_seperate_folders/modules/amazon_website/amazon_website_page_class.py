import pytest
from base.selenium_base_class import SeleniumBase
from .amazon_website_locator import *

class AmazonWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def new_user_account(self):
        self.click_element(new_customer)

    def create_amazon_account(self):
        self.click_element(create_account)

    def enter_name(self, fullname):
        self.send_text(name_field, fullname)

    def enter_email_id(self, email):
        self.send_text(email_id, email)

    def enter_password(self, password):
        self.send_text(password_field, password)

    def reenter_password(self, reenter_pwd):
        self.send_text(reenter_password, reenter_pwd)

    def verify_email_id(self):
        self.click_element(verify_email)