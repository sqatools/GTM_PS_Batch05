import time
"""
module name to run the test cases parallel
pip install pytest-xdist

"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators_file import *
from resource_data_file import *


@pytest.mark.usefixtures("get_driver")
@pytest.mark.parametrize("firstname, lastname, dob", [('John', 'Jenny', '09/06/2000'),
                                                 ('Mohit', 'Sharma', '01/02/1909')])
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self, firstname, lastname, dob):
        self.first_name = firstname
        self.last_name = lastname
        self.date_of_birth = dob

    def get_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(ec.presence_of_element_located(locator))

    def test_enter_passenger_details(self):
        element_fname = self.get_element(first_name_locator)
        element_fname.clear()
        element_fname.send_keys(self.first_name)
        elem_lname = self.get_element(last_name_locator)
        elem_lname.clear()
        elem_lname.send_keys(self.last_name)

    def test_enter_dob(self):
        dob_elem = self.get_element(dob_calender)
        dob_elem.clear()
        dob_elem.send_keys(self.date_of_birth)

    def test_select_male_radio(self):
        self.get_element(male_radio_btn).click()

    def test_enter_travel_details(self):
        add_more_pass_element = self.get_element(add_more_pass_dd)
        select_obj = Select(add_more_pass_element)
        select_obj.select_by_visible_text(add_more_pass_details)

    def test_select_trip_type(self):
        self.get_element(one_way_radio).click()

    def test_enter_source_dest_city(self):
        from_city_element = self.get_element(from_city_field)
        from_city_element.clear()
        from_city_element.send_keys(source_city)

        dest_city_elem = self.get_element(dest_city_field)
        dest_city_elem.clear()
        dest_city_elem.send_keys(dest_city)

    def test_enter_depart_date(self):
        depart_date_elem = self.get_element(depart_date_calender)
        depart_date_elem.clear()
        depart_date_elem.send_keys(depart_date)

    def test_enter_return_date(self):
        return_date_elem = self.get_element(return_date_calender)
        return_date_elem.clear()
        return_date_elem.send_keys(return_date)
