from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Edge browser
driver = webdriver.Edge()
driver.implicitly_wait(20)
driver.maximize_window()

# Open google page on the browser
driver.get('https://www.google.co.in')

# Send text to google search field
driver.find_element(By.NAME, 'q').send_keys('Selenium automation')

# Click on search button
driver.find_element(By.NAME, 'btnK').click()

# Close browser
driver.close()
