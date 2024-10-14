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

    def existing_cust_sign_in(self, existing_cust_email_id, ex_cust_password_field):
        self.click_element(existing_customer)
        self.send_text(existing_cust_email, existing_cust_email_id)
        self.click_element(continue_button)
        self.send_text(existing_cust_password, ex_cust_password_field)
        self.click_element(sign_in_button)

    def edit_profile_information(self, enter_apt_no):
        self.click_element(account_lists)
        self.click_element(your_addresses)
        self.click_element(edit_address)
        self.send_text(edit_apt_no, enter_apt_no)

    def search_for_products1(self, enter_product1):
        self.send_text(search_amazon1, enter_product1)
        self.click_element(search_entered_product1)
        #self.click_element(filter_by_prime)
        self.click_element(filter_by_brands)
        #self.click_element(sort_by)

    def add_items_to_cart(self):
        self.click_element(selected_product1)
        self.click_element(add_to_cart1)

    def search_for_products2(self, enter_product2):
        self.send_text(search_amazon2, enter_product2)
        self.click_element(search_entered_product2)
        self.click_element(selected_product2)
        self.click_element(add_to_cart2)
        self.click_element(go_to_cart)
        self.click_element(remove_item)






