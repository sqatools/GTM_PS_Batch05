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


get_element(locator=(By.LINK_TEXT, "Software Testing Principles")).click()
browser_windows = driver.window_handles
print("browser windows :", browser_windows)

# switching to new browser tab
driver.switch_to.window(browser_windows[1])
element = get_element(locator=(By.XPATH, "//span[contains(text(), 'Exhaustive Testing is Not Possible')]"))
assert element
print(element.text)

# closing the new browser tab
driver.close()

# switching back to main window
driver.switch_to.window(browser_windows[0])
get_element(locator=(By.LINK_TEXT, "Monkey Testing")).click()


time.sleep(5)
driver.close()
