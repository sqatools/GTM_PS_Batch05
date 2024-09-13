import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
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

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

def drag_and_drop():
   # return wait.until(ec.visibility_of_element_located(locator))

    iframe_element = web_element(locator=(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
    driver.switch_to.frame(iframe_element)
    action = ActionChains(driver)
    image4= web_element(locator=(By.XPATH,"//h5[text()='High Tatras 4']//parent::li"))
    trash_element=web_element(locator=(By.XPATH,"//div[@id='trash']"))
    action.drag_and_drop(image4,trash_element)
    action.perform()
    time.sleep(5)

drag_and_drop()
