import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://automationbysqatools.blogspot.com/p/home.html")
element = driver.find_element(By.ID,"male")
print("check element is displayed:", element.is_displayed())
print("check element is selected before click:",element.is_selected())
element.click()
print("check element is selected after click:", element.is_selected())
print("check element is_enabled:", element.is_enabled())

