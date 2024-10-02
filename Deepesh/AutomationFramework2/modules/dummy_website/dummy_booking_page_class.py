import pytest
from base.selenium_base import SeleniumBase
from .dummy_booking_page_class_data import *


class DummyBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_firstname(self, firstname):
        self.send_text(first_name_field, firstname)

    def enter_lastname(self, lastname):
        self.send_text(last_name_field, lastname)

    def select_gender_radio(self):
        self.click_element(male_radio_button)

    def select_number_of_passenger_from_dd(self, dropdown_value):
        self.select_value_from_dropdown(num_passenger_dropdown, dropdown_value)
