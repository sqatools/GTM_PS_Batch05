import pytest
from base.selenium_base_class import SeleniumBase
from .dummy_booking_page_class_data_locator_file import *

class DummyBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def select_correct_option(self):
        self.click_element(correct_option)

    def enter_firstname(self, firstname):
        self.send_text(first_name, firstname)

    def enter_lastname(self, lastname):
        self.send_text(last_name, lastname)

    def enter_dob(self, dob_calendar):
        self.send_text(dob, dob_calendar)

    def select_gender_radio_btn(self):
        self.click_element(male_radio_button)

    def select_additional_passengers_from_dd(self, dropdown_value):
        self.select_value_from_dropdown(no_of_passenger_dropdown, dropdown_value)

    def roundtrip_radio_btn(self):
        self.click_element(round_trip)

    def enter_from_city(self, from_city_field):
        self.send_text(from_city, from_city_field)

    def enter_dest_city(self, dest_city_field):
        self.send_text(dest_city, dest_city_field)

    def enter_dept_date(self, depart_date_field):
        self.send_text(dept_date, depart_date_field)

    def enter_return_date(self, return_date_field):
        self.send_text(return_date, return_date_field)

    def enter_visa_interview(self, visa_appt_date):
        self.send_text(visa_interview, visa_appt_date)

    def select_receive_ticket_radio_btn(self):
        self.click_element(receive_ticket)

    def enter_billing_name(self, billing_name_field):
        self.send_text(billing_name, billing_name_field)

    def enter_phone(self, phone_field):
        self.send_text(phone, phone_field)

    def enter_email_address(self, email_address_field):
        self.send_text(email, email_address_field)

    def enter_street_address(self, street_address_field):
        self.send_text(address, street_address_field)

    def select_country_from_dd(self, country_dropdown_value):
        self.select_value_from_dropdown(country_dropdown, country_dropdown_value)

    def enter_postcode(self, post_code_field):
        self.send_text(postcode, post_code_field)

    def enter_street_address1(self, street_address1_field):
        self.send_text(street_address, street_address1_field)

    def select_most_visited_cities_radio_btn(self):
        self.click_element(most_visited_cities_radio_btn)
