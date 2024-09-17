from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

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

driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


links_text = ['Smoke Testing',
              'Monkey Testing',
              'Ad-hoc Testing',
              'Sanity Testing']
for text_value in links_text:
    get_element(locator=(By.LINK_TEXT, text_value)).click()

# get total browser tabs, which will be 5
windows_list = driver.window_handles

# switch to each window tab with the help of for loop.
for window_id in windows_list[1:]:
    driver.switch_to.window(window_id)
    print(driver.current_url)
    time.sleep(3)
    driver.close()

# switch to main browser tab.
driver.switch_to.window(windows_list[0])

# click to home link
get_element(locator=(By.XPATH, "//li/a[text()='Home']")).click()

time.sleep(5)
driver.close()
