import pytest
from modules.dummy_website.dummy_booking_page_class import DummyBooking


@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dummy_book = DummyBooking(self.driver)

    def test_dummy_booking(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dummy_book.enter_firstname('John')
        self.dummy_book.enter_lastname('jenny')
        self.dummy_book.select_gender_radio()
