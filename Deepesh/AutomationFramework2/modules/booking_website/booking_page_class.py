from base.selenium_base import SeleniumBase
from .booking_page_class_data import *


class BookingDotComPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def select_one_way_radio_button(self):
        self.click_element(one_way_radio_button)

    def enter_source_airport_name(self, city_name, airport_name):
        self.click_element(from_segment_button)
        self.send_text(airport_city_input_field, city_name)
        airport_selection = (By.XPATH, f"//span[text()='{airport_name}']")
        self.click_element(airport_selection)

    def enter_destination_airport_name(self, city_name, airport_name):
        self.click_element(to_segment_button)
        self.send_text(airport_city_input_field, city_name)
        airport_selection = (By.XPATH, f"//span[text()='{airport_name}']")
        self.click_element(airport_selection)

    def select_departure_date(self, travel_date):
        self.click_element(calender_locator)
        calender_date = (By.XPATH, f"//span[@data-date='{travel_date}']")
        self.click_element(calender_date)

    def add_number_of_passengers(self, adults, children):
        self.click_element(occupancy_of_passenger)
        for i in range(1, adults):
            self.click_element(add_num_of_adults)

        for i in range(0, children):
            self.click_element(add_num_of_children)

        self.click_element(done_button)

    def click_search_button(self):
        self.click_element(search_button)

    def search_flight(self, from_city,
                      source_airport,
                      dest_city,
                      dest_airport,
                      depart_date):
        self.select_one_way_radio_button()
        self.enter_source_airport_name(from_city, source_airport)
        self.enter_destination_airport_name(dest_city, dest_airport)
        self.select_departure_date(depart_date)
