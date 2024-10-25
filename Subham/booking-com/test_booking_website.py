import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("get_driver")
class TestBookingwWebsite:
    def test_filght_booking(self):
        self.driver.find_element(By.XPATH,"//a[@id='flights']").click()
        self.driver.find_element(By.XPATH,"(//span[@class='InputRadio-module__field___wQiXd'])[1]").click()
        self.driver.find_element(By.XPATH,"(//span[@class='ShellButton-module__contentInner___SbZm6'])[1]").send_keys("")




