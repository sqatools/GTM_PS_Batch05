import pytest
from base.selenium_base import SeleniumBase
from .dummy_booking_page_class_data import *


class DummyBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_firstname(self, firstname):
        self.log.info(f"Entering first name: {firstname}")
        self.send_text(first_name_field, firstname)

    def enter_lastname(self, lastname):
        self.log.info(f"Entering last name: {lastname}")
        self.send_text(last_name_field, lastname)

    def select_gender_radio(self):
        self.log.info(f"select male radio button")
        self.click_element(male_radio_button)

    def select_number_of_passenger_from_dd(self, dropdown_value):
        self.log.info(f"select number of passengers: {dropdown_value}")
        self.select_value_from_dropdown(num_passenger_dropdown, dropdown_value)
