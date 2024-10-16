import time

import pytest
from modules.makemytrip_website.makemytrip_page_class import MakeMyTripWebsite


@pytest.mark.usefixtures("get_driver")
class TestMakeMyTripWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.makemytrip_website = MakeMyTripWebsite(self.driver)

    def test_makemytrip_website(self):
        self.driver.get("https://www.makemytrip.com/")
        time.sleep(3)
        self.makemytrip_website.create_new_account()
        #time.sleep(3)
        self.makemytrip_website.dropdown_element()
       # self.makemytrip_website.select_country_code()
        self.makemytrip_website.create_acc_with_ph_no('7337879327')


#command: python -m pytest -v -s .\tests\makemytrip_website\test_makemytrip_website.py