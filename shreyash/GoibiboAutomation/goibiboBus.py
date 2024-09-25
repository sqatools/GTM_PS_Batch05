from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time

driver= webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver,timeout=20)

driver.get("https://www.goibibo.com/")

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))
#Auto Pop-up closing
get_element(locator=(By.XPATH,"//span[@role='presentation']")).click()
time.sleep(2)
#Clicking on Bus Section:
get_element(locator=(By.XPATH,"//span[text()='Bus']")).click()
time.sleep(2)
#Clicking on From city section:
get_element(locator=(By.XPATH,"//input[@placeholder='Enter Source']")).send_keys("Pune")
time.sleep(3)
#Adding from city value and selecting:
get_element(locator=(By.XPATH,"//span[text()='Pune, Maharashtra']")).click()
#Clicking on To city section:
get_element(locator=(By.XPATH,"//input[@placeholder='Enter Destination']")).send_keys("Banglore")
time.sleep(5)
#Selecting To city value and selecting:
get_element(locator=(By.XPATH,"//span[text()='Bangalore, Karnataka']")).click()
time.sleep(3)
#Click on Date section:
get_element(locator=(By.XPATH,"//input[@placeholder='Pick a date']")).click()
time.sleep(3)
#Adding Exact date for travelling:
get_element(locator=(By.XPATH,"//span[text()='27']")).click()
time.sleep(3)
#Clicking search button to check bus lists:
get_element(locator=(By.XPATH,"//button[text()='Search Bus']")).click()
time.sleep(3)

####Next Page###

#Sort by clicking on "Rating" option:
get_element(locator=(By.XPATH,"//span[@data-val='rating_high']")).click()
time.sleep(3)

#Sort by clicking on "Cheapest" option:
get_element(locator=(By.XPATH,"//span[@data-val='high_price']")).click()
time.sleep(3)

#Checking Boarding&Dropping points:
get_element(locator=(By.XPATH,"(//a[text()='Boarding & Dropping Points'])[1]")).click()
time.sleep(5)

#Scroll to "Sort" option:
def scroll_to_element():
    sort_info_element=get_element(locator=(By.XPATH,"//span[text()='Sort by:']"))
    action=ActionChains(driver)
    action.scroll_to_element(sort_info_element)
    action.perform()
    time.sleep(5)
scroll_to_element()

#Click on to "Hide Details":
get_element(locator=(By.XPATH,"//a[text()='Hide Details']")).click()
time.sleep(3)

#Click on Select Seat button:
get_element(locator=(By.XPATH,"(//span[text()='SELECT SEAT'])[1]")).click()
time.sleep(3)

#Droping point while selecting seat:
get_element(locator=(By.XPATH,"//p[text()='Dropping Point']//following-sibling::div//label[2]")).click()
time.sleep(3)

#Select Seat from upper section:
get_element(locator=(By.XPATH,"(//div[@class='SeatWithTooltipstyles__BusSleeper-sc-dkrka-1 cukzzY'])[1]")).click()
time.sleep(3)

#click on "Continue" button to book seat:
get_element(locator=(By.XPATH,"//button[text()='CONTINUE']")).click()
time.sleep(3)

###Next Page:Traveller Details###

#Select insure trip facility:
get_element(locator=(By.XPATH,"//span[text()='No, I am willing to risk my trip']")).click()
time.sleep(3)

#Scroll to "Traveller 1" option:


#Title traveller details:
get_element(locator=(By.XPATH,"//span[text()='Traveller Details']")).click()
time.sleep(2)


def scroll_to_element():
    traveller_info_element1 = get_element(locator=(By.XPATH, "//span[text()='ENTER PROMO CODE ']"))
    action = ActionChains(driver)
    action.scroll_to_element(traveller_info_element1)
    action.perform()
    time.sleep(5)


scroll_to_element()

#Adding FullName details:
get_element(locator=(By.XPATH,"//input[@placeholder='Enter Full Name']")).send_keys("San Adreas")
time.sleep(3)