import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(20)

driver.get("https://www.irctc.co.in/nget/train-search")

driver.find_element(By.NAME,"email").send_keys("Testadmin")
driver.find_element(By.NAME,"pass").send_keys("Admin@123")

time.sleep(5)

driver.find_element(By.NAME,"login").click()