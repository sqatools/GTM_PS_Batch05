import time
import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    # @pytest.fixture(scope='class')
    # def get_driver(self, request):
    #     driver = webdriver.Chrome()
    #     driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    #     driver.maximize_window()
    #     driver.implicitly_wait(20)
    #     # hold value of driver in driver variable  for any class
    #     self.driver = driver
    #     yield
    #     driver.close()

    def test_enter_user_deatils(self):
        self.driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()
        self.driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Subham")
        self.driver.find_element(By.XPATH,"(//input[@id='[irstname'])[2]").send_keys("Behera")
        self.driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("05/23/1993")
        self.driver.find_element(By.XPATH,"//input[@id='male']").click()
        time.sleep(10)

    def test_enter_add_pass_deatils(self):
        add_more_pass_dd = self.driver.find_element(By.XPATH,"//select[@id='admorepass']")
        select_obj = Select(add_more_pass_dd)
        select_obj.select_by_visible_text("Add 3 more passenger (200%)")
        time.sleep(10)

    def test_enter_add_travel_deatils(self):
        self.driver.find_element(By.XPATH,"//input[@id='roundtrip']").click()
        self.driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("delhi")
        self.driver.find_element(By.XPATH,"//input[@id='destcity']").send_keys("bhubaneswar")
        self.driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys("12/25/2024")
        self.driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys("12/31/2024")
        time.sleep(10)


    def test_enter_visa_deatils(self):
        self.driver.find_element(By.XPATH,"//input[@id='visadate']").send_keys("12/20/2024")
        time.sleep(10)

    def test_enter_ticket_deatils(self):
        self.driver.find_element(By.XPATH,"(//input[@id='female'])[2]").click()
        time.sleep(10)

    def test_enter_billng_deatils(self):
        self.driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("Subham Behera")
        self.driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("7008619711")
        self.driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("55subhambehera@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("cuttack odisha")
        add_con_deatils = self.driver.find_element(By.XPATH,"//select[@id='billing_country']")
        select_obj = Select(add_con_deatils)
        select_obj.select_by_index(13)
        self.driver.find_element(By.XPATH,"//input[@id='postcode']").send_keys("753001")
        self.driver.find_element(By.XPATH,"//input[@id='Prefecture']").send_keys("cuttack")
        self.driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys("c/o chiita ranjan behera pratima nivas")
        self.driver.find_element(By.XPATH,"//input[@id='street_address2']").send_keys("mangalbag cuttack")
        time.sleep(10)
    def test_enter_most_vist_deatils(self):
        self.driver.find_element(By.XPATH,"(//input[@type='checkbox'])[7]").click()
        time.sleep(10)

    def test_enter_contact_from_deatils(self):
        self.driver.find_element(By.XPATH,"//input[@id='ContactForm2_contact-form-name']").send_keys("subham behera")
        self.driver.find_element(By.XPATH,"//input[@id='ContactForm2_contact-form-email']").send_keys("55subhambehera@gmail.com")
        self.driver.find_element(By.XPATH,"//textarea[@id='ContactForm2_contact-form-email-message']").send_keys("thanku so much")
        self.driver.find_element(By.XPATH,"//input[@id='ContactForm2_contact-form-submit']").click()
        time.sleep(10)

    def test_enter_serach_deatils(self):
        self.driver.find_element(By.XPATH, "//input[@class='gsc-input']").send_keys("manual testing")
        self.driver.find_element(By.XPATH, "//input[@class='gsc-search-button']").click()
        time.sleep(10)






































































