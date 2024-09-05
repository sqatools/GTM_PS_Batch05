import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(20)
"""
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

element = driver.find_element(By.ID,"male")
print("check element is displayed:", element.is_displayed())
print("check element is selected before click:",element.is_selected())
element.click()
print("check element is selected after click:", element.is_selected())
print("check element is_enabled:", element.is_enabled())


""""""
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
header = driver.find_element(By.TAG_NAME, "h1")
print("header name:",header.text)
#link_test locator:
link_element = driver.find_element(By.LINK_TEXT, "Manual Testing")
print("href attribute value :", link_element.get_attribute("href"))
link_element.click()

time.sleep(5)

#partial_link text locator:

link_element_api = driver.find_element(By.PARTIAL_LINK_TEXT,"API")
print("API testing link:",link_element_api.get_attribute("href"))
link_element_api.click()

time.sleep(5)

#go back its previous page
driver.back()
time.sleep(5)

#forward to API testing
driver.forward()
time.sleep(5)

#URL for current website

print("website URL:",driver.current_URL)

#Get website title
print("website title:",driver.title)

"""
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#ID Locator:

fromcity_element = driver.find_element(By.ID,"fromcity").send_keys("Mumbai")

fromcity_element = driver.find_element(By.ID,"fromcity").clear()
time.sleep(5)
fromcity_element= driver.find_element(By.ID,"fromcity").send_keys("Pune")

time.sleep(5)
#Enter the date
depart_date = driver.find_element(By.ID,"departdate").send_keys("09/03/2024")

time.sleep(5)
driver.close()