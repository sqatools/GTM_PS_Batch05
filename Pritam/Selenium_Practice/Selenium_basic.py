
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# ID locator (use '#' for search)
element = driver.find_element(By.ID, "male")
print("Check element is displayed:", element.is_displayed()) # True
print("Check if element is selected before clicked:", element.is_selected()) # False
element.click()
time.sleep(5)
print("Check if element is selected after clicked:", element.is_selected()) # True
print("Check if element is enabled:", element.is_enabled()) # True

# TAG_NAME Locator (use '//' for search)
header_element = driver.find_element(By.TAG_NAME, "h1")
print("Header name:", header_element.text) # Header name: Dummy Ticket Booking Website

# LINK_TEXT Locator (use "// a[text() = 'API']" for search
link_element = driver.find_element(By.LINK_TEXT, "Manual Testing")
print("href attribute value is:", link_element.get_attribute("href"))
link_element.click()

time.sleep(5)
# PARTIAL_LINK_TEXT Locator
partial_link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "API")
print("href attribute value is:", partial_link_element.get_attribute("href"))
partial_link_element.click()
time.sleep(5)

# go back to previous page
driver.back() # manual testing
time.sleep(5)

# forward to API testing tutorials
driver.forward()

# URL for current website
print("Current url:", driver.current_url)

# Get website title
print("Title:", driver.title)
time.sleep(5)

# go back to dummy website page
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# ID Locator
fromcity_element = driver.find_element(By.ID, "fromcity")
fromcity_element.send_keys("Delhi")
fromcity_element.clear() # clear previously added value from text field
fromcity_element.send_keys("Bangalore")

dest_city = driver.find_element(By.ID, "destcity").send_keys("Kerala")
#driver.find_element(By.ID, "destcity").send_keys("Kerala")

# Enter the date with send keys
depart_date = driver.find_element(By.ID, "departdate")
depart_date.send_keys("10/09/2024")

return_date = driver.find_element(By.ID, "returndate")
return_date.send_keys("24/09/2024")
time.sleep(5)

# deal with list of elements
checkbox_list = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for element in checkbox_list:
    element.click()

time.sleep(5)

driver.close()
