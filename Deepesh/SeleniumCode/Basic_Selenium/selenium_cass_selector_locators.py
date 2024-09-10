import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
CSS_SELECTOR = "css selector"
1. ID
    -> #fromcity
2. Class
   -> .classname
3. attribute
   -> tagname[attribute='value']
   
4. sub-string
   -> tagname[attribute^='partial value']

"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# identify element by class name:
header = driver.find_element(By.CLASS_NAME, "post-title")
print(header.text)

#1. ID css selector #id_value
#
from_city = driver.find_element(By.CSS_SELECTOR, "#fromcity")
from_city.send_keys("Mumbai")

#2. class css selector .classname
header = driver.find_element(By.CSS_SELECTOR, ".post-title.entry-title")
print(header.text)

radio_button = driver.find_element(By.XPATH, "//span[text()='Both']//preceding-sibling::input[@id='female']")
radio_button.click()

#3. Attribute : tagname[attribute=value]
dest_city = driver.find_element(By.CSS_SELECTOR, "input[name='destcity']")
dest_city.send_keys("Bangalore")


#4. Substring of any attribute : tagname[attribute^, 'attrib value']
# ninput[name^='dest']
# div > input[id^='departdate']
dest_city2 = driver.find_element(By.CSS_SELECTOR, "input[name^='dest']")
dest_city2.clear()
dest_city2.send_keys("Chennai")

time.sleep(10)
driver.close()
