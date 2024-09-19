import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
browser = 'chrome'
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

driver.get("https://www.globalsqa.com/")

def web_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

def scroll_to_element():
    contact_element=web_element(locator=(By.XPATH,"//h3[text()='About Us']"))
    action=ActionChains(driver)
    action.scroll_to_element(contact_element)
    action.perform()
    time.sleep(5)

scroll_to_element()







