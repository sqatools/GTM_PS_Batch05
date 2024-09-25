from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

import time

driver= webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver,timeout=20)

driver.get("https://www.goibibo.com/")

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

get_element(locator=(By.XPATH,"//span[@role='presentation']")).click()
time.sleep(2)

Flights_element=get_element(locator=(By.XPATH,"//span[text()='Flights']"))
print(Flights_element.text)
time.sleep(2)
#roundtripbutton:
get_element(locator=(By.XPATH,"(//span[@class='sc-12foipm-70 bWWMhV'])[1]")).click()
time.sleep(2)
#Fromcity:
fromcity_element=get_element(locator=(By.XPATH,"//span[text()='From']//following-sibling::p")).click()
time.sleep(2)
#FromCity value enter:
EnterCity_element=get_element(locator=(By.XPATH,"//span[text()='From']//following-sibling::input")).send_keys("New Delhi")
time.sleep(3)
#Tocity:
#ToCity_element=get_element(locator=(By.XPATH,"//span[text()='To']//following-sibling::input")).send_keys("Pune")
#time.sleep(4)
#departuredateclick:
get_element(locator=(By.XPATH,"//span[text()='Departure']")).click()
time.sleep(2)
#Add Depatrure date:
get_element(locator=(By.XPATH,"//div[contains(@aria-label,'Mon Sep 23 2024')]")).click()
time.sleep(3)
#return date select:
#get_element(locator=(By.XPATH,"//span[text()='Return']")).click()
#time.sleep(2)
#returndate:
get_element(locator=(By.XPATH,"//div[contains(@aria-label,'Tue Oct 01 2024')]")).click()
time.sleep(4)
#Adults Entry:
get_element(locator=(By.XPATH,"//span[@class='sc-12foipm-8 eXKWBG fswDownArrow fswDownArrowTraveller']")).click()
time.sleep(3)
#AdultTab:
get_element(locator=(By.XPATH,"//p[text()='Adults']")).click()
time.sleep(3)
#add adult values:
get_element(locator=(By.XPATH,"//p[text()='Adults']//following-sibling::div/span[3]")).click()
time.sleep(3)
#Done button close add traveller tab:
get_element(locator=(By.XPATH,"//a[text()='Done']")).click()
time.sleep(3)
#search button
get_element(locator=(By.XPATH,"//span[text()='SEARCH FLIGHTS']")).click()
time.sleep(3)