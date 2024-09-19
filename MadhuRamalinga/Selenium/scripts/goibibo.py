import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.goibibo.com/")
wait = WebDriverWait(driver, timeout=30)
time.sleep(5)


def web_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

'''alert1 = Alert(driver)
web_element(locator=(By.XPATH, 'span//[@role="presentation"]')).click()
time.sleep(5)
alert1.dismiss()'''

'''web_element(locator=(By.CSS_SELECTOR, ".sc-12foipm-70.fPPRk")).click() # Round-trip
web_element(locator=(By.XPATH,"(//p[contains(text()='Enter City')])[1]")).send_keys("Bangalore") # From
web_element(locator=(By.XPATH,"(//p[contains(text()='Enter City')])[2]")).send_keys("Delhi") # To'''

web_element(locator=(By.XPATH, "//span[text()='from']//following-sibling::p[text()='Enter city or airport']")).send_keys("Bangalore")

# //span[text()='From']//following-sibling::p
# //span[text()='From']//following-sibling::input
# //p[text()='Adults']//following-sibling::div/span[3]
# //p[text()='Infants']//following-sibling::div/span[3]

# https://www.w3schools.com/jsref/dom_obj_all.asp

time.sleep(5)
driver.close()
