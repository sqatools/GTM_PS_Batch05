import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
# Done : ID = "id"
XPATH = "xpath"
# Done : LINK_TEXT = "link text"
# DONE : PARTIAL_LINK_TEXT = "partial link text"
# Done : NAME = "name"
# Done : TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# identify element by class name:
header = driver.find_element(By.CLASS_NAME, "post-title")
print(header.text)

radio_button = driver.find_element(By.XPATH, "//span[text()='Both']//preceding-sibling::input[@id='female']")
radio_button.click()
time.sleep(10)
driver.close()
