import time

import pytest
from bookingdotcom_class import BookingDotComPage

@pytest.mark.usefixtures("get_driver")
class TestBookingWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.booking_website = BookingDotComPage(self.driver)

    def test_booking_website(self):
        self.driver.get("https://www.booking.com/flights/")
        time.sleep(3)
        self.booking_website.select_one_way_radio_button()
        time.sleep(3)
        self.booking_website.enter_source_airport_name('Pune')
        time.sleep(3)
        self.booking_website.enter_destination_airport_name('Delhi')
        time.sleep(3)
        self.booking_website.enter_depart_date()
        time.sleep(3)
        self.booking_website.enter_no_of_travellers('1')
        time.sleep(5)
        self.booking_website.filter_results()
        time.sleep(3)
        self.booking_website.view_selected_flight_details()
        time.sleep(3)
        self.booking_website.enter_traveler_details1('Shre', 'Man', 'Male')
        time.sleep(3)
        self.booking_website.enter_contact_details('shreyasbhokare43@gmail.com', '8698697807')