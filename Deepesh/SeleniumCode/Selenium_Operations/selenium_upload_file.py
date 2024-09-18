from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

"""
DOM Queries:
https://www.w3schools.com/jsref/dom_obj_all.asp

"""
import pdb; pdb.set_trace()

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

driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")

driver.find_element(By.ID, "myFile").send_keys("E:\\Filesdata\\batch05\\count_name.txt")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@id='myFile']//following-sibling::input[@type='submit']").click()
time.sleep(5)

driver.close()


