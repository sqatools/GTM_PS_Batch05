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

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


get_element(locator=(By.CSS_SELECTOR, "input[name^='from']")).send_keys("Mumbai")
get_element(locator=(By.CSS_SELECTOR, "input[name^='dest']")).send_keys("Kolkata")
get_element(locator=(By.CSS_SELECTOR, "input[id^='billing_name']")).send_keys("John")

dd_element = get_element(locator=(By.ID, "billing_country"))
select_obj = Select(dd_element)
select_obj.select_by_visible_text("India")

# take screen completed window after selecting the value from dropdown
driver.save_screenshot("E:\\Filesdata\\batch05\\country_dd.png")

pass_dd_elem = get_element(locator=(By.ID, "admorepass"))

# take a screenshot of specific element
pass_dd_elem.screenshot("add_more_pass_dropdown.png")
select2 = Select(pass_dd_elem)
select2.select_by_visible_text("Add 3 more passenger (200%)")

time.sleep(5)
driver.close()
