import time

import pytest
from base.selenium_base_class import SeleniumBase
from .booking_dotcom_page_class_data_locator import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class BookingDotComPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        ec.visibility_of_element_located(locator))

    def select_one_way_radio_button(self):
        self.click_element(one_way_radio_btn)

    def enter_source_airport_name(self, city_name):
        self.click_element(from_city)
        self.click_element(close_default_selection)
        self.send_text(from_airport_city, city_name)
        #airport_selection = (By.XPATH, f"//span[text()='{airport_name}']")
        self.click_element(from_airport_city_selection)

    def enter_destination_airport_name(self, dest_city_name):
        self.click_element(dest_city)
        self.send_text(to_airport_city, dest_city_name)
        #dest_airport_selection = (By.XPATH, f"//span[text()='{dest_airport}']")
        self.click_element(to_airport_city_selection)

    def enter_depart_date(self):
        self.click_element(depart_date)
        self.click_element(depart_date_selection)

    def enter_no_of_travellers(self, dropdown_value):
        self.click_element(no_of_passengers)
        self.click_element(no_of_adults_selection)
        self.click_element(no_of_children_selection)
        self.select_value_from_dropdown(child_age_dd, dropdown_value)
        self.click_element(no_of_passengers_selection_done)
        self.click_element(search_button)

    def filter_results(self):
        self.click_element(direct_only)
        #self.click_element(air_india_express)
        #self.click_element(regional_air)

    def view_selected_flight_details(self):
        self.click_element(view_details)
        self.click_element(select_flight)
        self.click_element(std_ticket)
        self.click_element(next_button)

    def enter_traveler_details1(self, adult1_fn, adult1_ln, gender1_dd):
        self.click_element(traveler_details1)
        time.sleep(5)
        self.wait_for_element_to_be_visible(first_name1, timeout=10)
        self.send_text(first_name1, adult1_fn)
        self.send_text(last_name1, adult1_ln)
        self.select_value_from_dropdown(gender_element1, gender1_dd)
        #self.send_text(dob1_date, adult1_date)
        #self.select_value_from_dropdown(dob1_month, adult1_month)
        #self.send_text(dob1_year, adult1_year)
        self.click_element(done_button1)

    def enter_traveler_details2(self, adult2_fn, adult2_ln, gender2_dd):
        self.click_element(traveler_details2)
        time.sleep(3)
        self.wait_for_element_to_be_visible(first_name2, timeout=10)
        self.send_text(first_name2, adult2_fn)
        self.send_text(last_name2, adult2_ln)
        self.select_value_from_dropdown(gender_element2, gender2_dd)
        self.click_element(done_button2)

    def enter_child_details(self, ch_fn, ch_ln, ch_gender_dd, date, month_dd, year):
        self.click_element(child_details)
        #time.sleep(3)
        self.wait_for_element_to_be_visible(child_fn, timeout=10)
        self.send_text(child_fn, ch_fn)
        self.send_text(child_ln, ch_ln)
        self.select_value_from_dropdown(child_gender, ch_gender_dd)
        self.send_text(dob_date, date)
        dob_month_element = self.get_element(dob_month)
        #self.select_value_from_dropdown(dob_month, month_dd)
        select_month = Select(dob_month_element)
        select_month.select_by_visible_text(month_dd)
        self.send_text(dob_year, year)
        self.click_element(done_button3)

    def enter_contact_details(self, contact_email, ph_no):
        self.send_text(contact_details, contact_email)
        #self.select_value_from_dropdown(country_code_dd, cc_dd)
        self.send_text(phone_number, ph_no)
        self.wait_for_element_to_be_visible(next_button_details_page, timeout=10)
        self.click_element(next_button_details_page)
        self.wait_for_element_to_be_visible(next_button_travel_ins, timeout=10)
        self.click_element(next_button_travel_ins)
        time.sleep(5)
        self.click_element(skip_button)











