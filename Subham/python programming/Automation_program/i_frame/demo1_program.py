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

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

def drag_and_Drop():
    iframe_element = get_element(locator=(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
    driver.switch_to.frame(iframe_element)
    action = ActionChains(driver)
    image2= get_element(locator=(By.XPATH,"//h5[text()='High Tatras 2']//parent::li"))
    trash_element=get_element(locator=(By.XPATH,"//div[@id='trash']"))
    action.drag_and_drop(image2,trash_element)
    action.perform()

    for i in range(2,5):
        image2 = get_element(locator=(By.XPATH, f"//h5[text()='High Tatras 2 {i}']//parent::li"))
        action.drag_and_drop(image2, trash_element)
        action.perform()
        time.sleep(5)



drag_and_Drop()





