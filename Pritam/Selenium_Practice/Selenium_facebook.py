import time
from selenium import webdriver
from selenium.webdriver .common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.facebook.com/login/")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@id=email").send_keys("Pritampawan009@gmail.com");
driver.find_element(By.XPATH,"//input[@id=pass").send_keys("Pritam@09");
driver.find_element(By.XPATH,"//input@id=loginbutton").click();
driver.find_element(By.XPATH,"//input@text()=Forgot").click();
driver.find_element(By.XPATH,"//input@text()=Sign up for Facebook").click();
time.sleep(2)
driver.close()