import time

import pytest
from modules.amazon_website.amazon_website_page_class import AmazonWebsite


@pytest.mark.usefixtures("get_driver")
class TestAmazonWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.amazon_website = AmazonWebsite(self.driver)

    def test_amazon_website(self):
        self.driver.get("https://www.amazon.com/")
        self.amazon_website.new_user_account()
        self.amazon_website.create_amazon_account()
        self.amazon_website.enter_name('Madhu')
        self.amazon_website.enter_email_id('madhu.ramalinga1524@gmail.com')
        self.amazon_website.enter_password('MadhuTesting')
        self.amazon_website.reenter_password('MadhuTesting')
        self.amazon_website.verify_email_id()
        #time.sleep(5)
        #self.driver.close()
