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

website_url = driver.execute_script("return document.title;")
print(website_url)

time.sleep(5)
from_city_element = driver.execute_script("return document.getElementById('fromcity');")
from_city_element.send_keys("Mumbai")

dest_city_element = driver.execute_script("return document.getElementById('destcity');")
dest_city_element.send_keys("Bangalore")

time.sleep(5)

# home = driver.execute_script("return document.getElementByXPATH("(//a[text()='Home'])[1];")
# home.click

dob = driver.execute_script("return document.getElementById('birthday').tagName;") #DOB
print(dob)

time.sleep(5)
scroll_top = driver.execute_script("return document.getElementById('post-body-5123879497792889300').scrollTop;")
scroll_top

title_text = driver.execute_script("return document.getElementByXPath('//h1[@align='center']').textContent;") #  Dummy Ticket Booking Website
print(title_text)