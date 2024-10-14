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
        time.sleep(5)

        '''self.amazon_website.new_user_account()
        self.amazon_website.create_amazon_account()
        self.amazon_website.enter_name('Madhu')
        self.amazon_website.enter_email_id('madhu.ramalinga1524@gmail.com')
        self.amazon_website.enter_password('MadhuTesting')
        self.amazon_website.reenter_password('MadhuTesting')
        self.amazon_website.verify_email_id()'''

        self.amazon_website.existing_cust_sign_in('madhu.ramalinga1524@gmail.com', 'MadhuTesting')
        self.amazon_website.edit_profile_information('1538')
        self.amazon_website.search_for_products1('dog toys')
        self.amazon_website.add_items_to_cart()
        self.amazon_website.search_for_products2('dog treats')

        time.sleep(5)


#command - python -m pytest -v -s .\tests\amazon_website\test_amazon_website.py

