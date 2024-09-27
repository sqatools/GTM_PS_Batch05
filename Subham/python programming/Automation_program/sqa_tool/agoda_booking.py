import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#explicit wait
from selenium.webdriver.support import expected_conditions as ec
#select dropdown
from selenium.webdriver.support.select import Select
browser = 'chrome'
driver = None

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()

driver.maximize_window()
wait = WebDriverWait(driver, timeout=30)

driver.get("https://www.agoda.com/?site_id=1914935&tag=649ad788-f3ef-4930-96c0-fc4f648eb89a&device=c&network=o&msclkid=e7b42ecaff6c13f162d8483b8d8271fd&checkIn=2024-10-02&checkOut=2024-10-03&adults=1&rooms=1&pslc=1&ds=zL0GCFOF6sP6YOhW")
print(driver.title)
time.sleep(5)

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

#serach for hotel
get_element(locator=(By.XPATH,"//input[@aria-label='Enter a destination or property']")).send_keys("Pahalgam")
time.sleep(2)

#serach for hotel
get_element(locator=(By.XPATH,"//li[@class='Suggestion Suggestion__categoryName'][2]")).click()
time.sleep(2)

#book a date
get_element(locator=(By.XPATH,"//span[@data-selenium-date='2024-10-26']")).click()
time.sleep(2)

#book a date
get_element(locator=(By.XPATH,"//div[@data-date='2024-10-27']")).click()
time.sleep(2)

#how many people and room
get_element(locator=(By.XPATH,"//span[@role='button']")).click()
time.sleep(2)

get_element(locator=(By.XPATH,"//div[@data-selenium='occupancyRooms']")).send_keys(2)
















