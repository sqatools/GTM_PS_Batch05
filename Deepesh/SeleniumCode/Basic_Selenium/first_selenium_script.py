"""
pip install selenium
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch a browser
driver = webdriver.Chrome()
# maximize browser window
driver.maximize_window()
#  set implicit wait for 20 sec.
driver.implicitly_wait(20)
# open a facebook URL in the browser
driver.get("https://www.facebook.com")
driver.find_element(By.NAME, "email").send_keys("TestAdmin")
driver.find_element(By.NAME, "pass").send_keys("Admin@12345")
driver.find_element(By.NAME, "login").click()
# wait for 10 sec.
driver.close()
