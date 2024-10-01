import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators_file import *
from resource_data_file import *


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    def get_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(ec.presence_of_element_located(locator))

    def test_enter_passenger_details(self):
        self.get_element(first_name_locator).send_keys(first_name_value)
        self.get_element(last_name_locator).send_keys(last_name_value)

    def test_enter_dob(self):
        self.get_element(dob_calender).send_keys(dob)

    def test_select_male_radio(self):
        self.get_element(male_radio_btn).click()

    def test_enter_travel_details(self):
        add_more_pass_element = self.get_element(add_more_pass_dd)
        select_obj = Select(add_more_pass_element)
        select_obj.select_by_visible_text(add_more_pass_details)

    def test_select_trip_type(self):
        self.get_element(one_way_radio).click()

    def test_enter_source_dest_city(self):
        self.get_element(from_city_field).send_keys(source_city)
        self.get_element(dest_city_field).send_keys(dest_city)

    def test_enter_depart_date(self):
        self.get_element(depart_date_calender).send_keys(depart_date)

    def test_enter_return_date(self):
        self.get_element(return_date_calender).send_keys(return_date)