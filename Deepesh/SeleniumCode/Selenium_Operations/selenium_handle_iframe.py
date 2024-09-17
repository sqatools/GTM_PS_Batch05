from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# We have to import a Select class to handle dropdown
from selenium.webdriver.support.select import Select

import time

browser = 'edge'
driver = None

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()
elif browser.lower() == 'edge':
    driver = webdriver.Edge()

driver.maximize_window()
# explicit wait
wait = WebDriverWait(driver, timeout=20)

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


iframe_element = get_element(locator=(By.XPATH, "//iframe[@name='globalSqa']"))
driver.switch_to.frame(iframe_element)

header_email = get_element(locator=(By.XPATH, "//div[@class='header_mail']"))
print(header_email.text)

menu_option = get_element(locator=(By.ID, "mobile_menu_toggler"))
menu_option.click()
time.sleep(3)

# switch to main page
driver.switch_to.default_content()

tester_hub_elem = get_element(locator=(By.XPATH, "//div[@id='menu']//a[contains(text(),'Tester')]"))
tester_hub_elem.click()

time.sleep(10)
driver.close()
