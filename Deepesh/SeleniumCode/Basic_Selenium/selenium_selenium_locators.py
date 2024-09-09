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

# Selenium Method"

click
clear
send_keys
get_attribute
text
forward
back
title
current_url
is_enabled
is_selected
is_displayed
list of elements
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

"""
# ID locator
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
element = driver.find_element(By.ID, "male")
print("check element is displayed :", element.is_displayed()) # True
print("check element is selected before click:", element.is_selected()) # False
element.click()
print("check element is selected after click:", element.is_selected()) # True
print("check element is_enabled:", element.is_enabled()) # True

# TAG_NAME Locator
header_element = driver.find_element(By.TAG_NAME, "h1")
print("header name :", header_element.text)


# LINK_TEXT Locator
link_element = driver.find_element(By.LINK_TEXT, "Manual Testing")
print("href attribute value :", link_element.get_attribute("href"))
link_element.click()

time.sleep(5)
# PARTIAL_LINK_TEXT Locator
link_element_api = driver.find_element(By.PARTIAL_LINK_TEXT, "API Test")
print("API testing link :", link_element_api.get_attribute("href"))
link_element_api.click()

time.sleep(5)
# go back to previous page
driver.back()  # manual testing
time.sleep(5)

# forward to API testing tutorials
driver.forward()

# URL for current website
print("website URL :",driver.current_url)

# Get website title
print("website title :", driver.title)
"""

# go back to dummy website page
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# ID Locator
fromcity_element = driver.find_element(By.ID, "fromcity")
fromcity_element.send_keys("Mumbai")
fromcity_element.clear()  # clear previously added value from text field
fromcity_element.send_keys("Kolkata")

# Enter the date with send keys
depart_date = driver.find_element(By.ID, "departdate")
depart_date.send_keys("09/10/2024")

return_date = driver.find_element(By.ID, "returndate")
return_date.send_keys("09/15/2024")

# deal with list of elements

checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for element in checkbox_list:
    element.click()
    time.sleep(2)



time.sleep(10)

driver.close()


