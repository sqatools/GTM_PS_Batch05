
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.youtube.com/")
driver.find_element(By.NAME, "search_query").send_keys("leharado")
time.sleep(3)
driver.find_element(By.ID, "search-icon-legacy").click()
time.sleep(10)

driver.close()



