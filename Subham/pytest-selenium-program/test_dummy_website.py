import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from GTM_PS_Batch05.MadhuRamalinga.Pytest_Selenium.conftest import get_driver


@pytest.mark.usefixture("get_driver")
class TestDummyWebsite:

    def test_enter_user_deatils(self):
        self.driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()
        self.driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Subham")
        self.driver.find_element(By.XPATH,"(//input[@id='[irstname'])[2]").send_keys("Behera")
        self.driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("05/23/1993")
        self.driver.find_element(By.XPATH,"//input[@id="male"]").click()
        time.sleep()

    def test_enter_add_pass_deatils(self):
m