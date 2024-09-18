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

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

URL = driver.execute_script("return document.URL;")
print(URL)

website_title = driver.execute_script("return document.title;")
print(website_title)

from_city_element = driver.execute_script("return document.getElementById('fromcity');")
from_city_element.send_keys("Mumbai")

dest_city_element = driver.execute_script("return document.getElementById('destcity');")
dest_city_element.send_keys("Bangalore")

time.sleep(5)


