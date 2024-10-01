import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    def test_passenger_details(self):
        self.driver.find_element(By.XPATH, "(//input[@name='firstname'])[1]").send_keys("John")
        self.driver.find_element(By.XPATH, "(//input[@name='firstname'])[2]").send_keys("Jenny")
        self.driver.find_element(By.ID, "birthday").send_keys("04/06/1990")
        self.driver.find_element(By.ID, "male").click()

    def test_enter_travel_details(self):
        add_more_pass_dd = self.driver.find_element(By.ID, "admorepass")
        select_obj = Select(add_more_pass_dd)
        select_obj.select_by_visible_text("Add 3 more passenger (200%)")

        self.driver.find_element(By.ID, "oneway").click()
        self.driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
        self.driver.find_element(By.ID, "destcity").send_keys("Bangalore")

        self.driver.find_element(By.ID, "departdate").send_keys("29/09/2024")
        self.driver.find_element(By.ID, "returndate").send_keys("29/09/2024")
        time.sleep(10)
