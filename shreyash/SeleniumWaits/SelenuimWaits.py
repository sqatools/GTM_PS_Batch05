from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

wait = WebDriverWait(driver,timeout=20)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.CSS_SELECTOR,"input[name^='fromcity']").send_keys("Mumbai")

t1 = time.time()
try:

    driver.find_element(By.CSS_SELECTOR, "input[name^='dest']").send_keys("Banglore")

except:
    pass

t2 = time.time()
print("total time:",t2-t2)

a1 = time.time()
try:
    wait.until(ec.visibility_of_element_located((By.ID, "billing_name1"))).send_keys("Shreyas")
except:
    pass
a2 = time.time()
print("total time:",a2-a1)

time.sleep(5)
driver.close()



