import pytest
from modules.dummy_website.dummy_booking_page_class import DummyBooking


@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dummy_book = DummyBooking(self.driver)

    def test_dummy_booking(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dummy_book.select_correct_option()
        self.dummy_book.enter_firstname('Coco')
        self.dummy_book.enter_lastname('Melon')
        self.dummy_book.enter_dob('11/15/2023')
        self.dummy_book.select_gender_radio_btn()
        self.dummy_book.select_additional_passengers_from_dd("I'm the only one traveler")
        self.dummy_book.roundtrip_radio_btn()
        self.dummy_book.enter_from_city('Bangalore')
        self.dummy_book.enter_dest_city('Delhi')
        self.dummy_book.enter_dept_date('10/18/2024')
        self.dummy_book.enter_return_date('10/24/2024')
        self.dummy_book.enter_visa_interview('10/21/2024')
        self.dummy_book.select_receive_ticket_radio_btn()
        self.dummy_book.enter_billing_name('Coco')
        self.dummy_book.enter_phone('7337879327')
        self.dummy_book.enter_email_address('coco@gmail.com')
        self.dummy_book.enter_street_address('HAL Old Airport Road')
        self.dummy_book.select_country_from_dd('India')
        self.dummy_book.enter_postcode('560017')
        self.dummy_book.enter_street_address1('HAL, Bangalore')
        self.dummy_book.select_most_visited_cities_radio_btn()

#command - python -m pytest -v -s .\tests\dummy_website\test_dummy_booking.py