#make my trip

1)#image make my trip =//img[@alt="Make My Trip"]

2)#one way radio button = //li[@data-cy="roundTrip"]

3)#roud trip radio button =//li[@data-cy="mulitiCityTrip"]

4)# from = //input[@id="fromCity"]

5] #depature = //input[@id="departure"]

6]# hotel = >> //span[text()='Hotels']

7] #login = //p[@data-cy="LoginHeaderText"]

8]#language = //div[@data-cy="LanguageSwitcherWidget"]

9]#introducingbig = //span[@data-cy="myBizText"]

10]#booknow = //a[@data-cy="superOfferCtaText0"]

11]#t&c apply = //span[@data-cy="superOfferUrl0"]

12]#view all = //span[@data-cy="viewAllCta"]

13]#cab = //li[@data-cy="CABS"]

14] #forward button = //button[@type="button"]

15]#all Offers - //a[contains(@id,'superOffersTab_ALL')]

16]#select spcial image = //div[@class="titleTag "]

17]#radio button student = (//input[@type="radio"])[2]

18] banglor filght = (//div[@class="flexOne"])[8]

#following

#//li[@data-cy="roundTrip"]//following::li[@data-cy="CABS"]


#following sibling
#//li[@data-cy="HOLIDAYS"]//following-sibling::li[4]


#preceding:

#(//div[@class="flexOne"])[8]//preceding::input[@id="fromCity"]

#preceding- sibling

#//li[@data-cy="HOLIDAYS"]//preceding-sibling::li[1]


#parent

#//a[@id="superOffersTab_FLIGHTS"]//parent::li


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.maximize_window()
    driver.implicitly_wait(20)
    #hold value of driver in driver variable  for any class
    request.cls.driver = driver
    yield
    driver.close()






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































