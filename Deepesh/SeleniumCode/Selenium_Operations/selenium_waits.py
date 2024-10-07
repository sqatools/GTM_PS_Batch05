"""
implicit wait : Implicit wait applies on all the web elements on the web without any condition
explicit wait : explicit wait applies on specific element with specified condition. it is maximum
                timeout to look for element on the web page. if we found element in 0.5 sec or any short
                then it will perform operation and move ahead.

fluent wait : fluent wait is the poll frequency in explicit wait to check for the element
              is available or not, the default poll frequency is 0.5 sec.


static wait : This wait pause the script execution for given period of time, without any condition
              time.sleep(10)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(10)

# explicit wait
wait = WebDriverWait(driver, timeout=20, poll_frequency=2)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.CSS_SELECTOR, "input[name^='fromcity']").send_keys("Mumbai")
time.sleep(10) # static wait

t1 = time.time()
try:
    driver.find_element(By.CSS_SELECTOR, "input[name^='dest']").send_keys("Bangalore")
except:
    pass
t2 = time.time()
print("total timeout :", t2-t1)

a1 = time.time()
try:
    wait.until(ec.visibility_of_element_located((By.ID, "billing_name"))).send_keys("John")
    wait.until(ec.visibility_of_element_located((By.ID, "billing_name"))).send_keys("John")
except:
    pass
a2 = time.time()
print("total time for billing name :", a2 -a1)

driver.close()

