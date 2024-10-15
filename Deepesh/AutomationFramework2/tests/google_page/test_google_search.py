import time

import pytest
from modules.google_page.google_page_class import GooglePage


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GooglePage(self.driver)

    @pytest.mark.google
    def test_search_on_google(self):
        self.gp.open_google_page("https://google.co.in")
        self.gp.enter_value_to_search_box("Python Selenium")
        self.gp.click_to_search_button()
        time.sleep(5)
