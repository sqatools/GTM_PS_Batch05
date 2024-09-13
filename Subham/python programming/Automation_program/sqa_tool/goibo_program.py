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

driver.get("https://www.goibibo.com")
print(driver.title)
time.sleep(5)

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


get_element(locator=(By.CSS_SELECTOR,"span[role='presentation']")).click()
logo = get_element(locator=(By.CSS_SELECTOR,"span[class='sc-1f95z5i-8 gnkTau header-sprite logo gi-logo']"))
print(logo.text)
flight_text = get_element(locator=(By.XPATH,"//h2[text()='Domestic and International Flights']"))
print(flight_text.text)
time.sleep(2)
get_element(locator=(By.CSS_SELECTOR,"span[class='sc-12foipm-70 fPPRk']")).click()
get_element(locator=(By.XPATH,"(//p[@class='sc-12foipm-6 erPfRs'])[1]")).send_keys("mumbai")









