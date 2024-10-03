import pytest
from modules.dummy_website.dummy_booking_page_class import DummyBooking

@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dummy_book = testDummyBooking(self.driver)

    def test_dummy_booking(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dummy_book.select_correct_option()
        self.dummy_book.enter_firstname('Pritam')
        self.dummy_book.enter_lastname('Pawan')
        self.dummy_book.enter_dob('11/13/2021')
        self.dummy_book.select_gender_radio_btn()
        self.dummy_book.select_additional_passengers_from_dd()
        self.dummy_book.roundtrip_radio_btn()
        self.dummy_book.enter_from_city('Bangalore')
        self.dummy_book.enter_dest_city('Pune')
        self.dummy_book.enter_dept_date('10/17/2024')
        self.dummy_book.enter_return_date('10/24/2024')
        # self.dummy_book.enter_visa_interview('10/21/2024')
        # self.dummy_book.select_receive_ticket_radio_btn()
        self.dummy_book.enter_billing_name('Pritam')
        self.dummy_book.enter_phone('7760168991')
        self.dummy_book.enter_email_address('pritampawan009@gmail.com')
        self.dummy_book.enter_street_address('HSR Layout')
        self.dummy_book.select_country_from_dd()
        self.dummy_book.enter_postcode('560036')
        self.dummy_book.enter_street_address1('HSR, Bangalore')
        self.dummy_book.select_most_visited_cities_radio_btn()