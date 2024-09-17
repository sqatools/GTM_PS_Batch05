from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

browser = 'edge'
driver = 'none'

if browser.lower()== 'chrome':
    driver=webdriver.Chrome()
elif browser.lower()== 'firefox':
    driver=webdriver.Firefox()
elif browser.lower()== 'edge':
    driver=webdriver.Edge()
driver.maximize_window()

wait = WebDriverWait(driver,timeout=20)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

get_element (locator=(By.CSS_SELECTOR,"input[name^='fromcity']")).send_keys("Mumbai")

get_element (locator=(By.CSS_SELECTOR, "input[name^='dest']")).send_keys("Banglore")

get_element (locator=(By.CSS_SELECTOR, "input[id^=billing_name]")).send_keys("Shreyas")
time.sleep(5)
driver.close()


