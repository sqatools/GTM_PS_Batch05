from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

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


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


def perform_hover_operation():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    action = ActionChains(driver)
    testers_hub_elem = get_element(locator=(By.XPATH, "//div[@id='menu']//a[contains(text(),'Tester')]"))
    action.move_to_element(testers_hub_elem)
    action.perform()
    time.sleep(2)

    demo_site_elem = get_element(locator=(By.XPATH, "//span[text()='Demo Testing Site']"))
    action.move_to_element(demo_site_elem)
    action.perform()
    time.sleep(5)

    alert_elem = get_element(locator=(By.XPATH, "//span[text()='AlertBox']//parent::a"))
    action.click(alert_elem)
    action.perform()
    time.sleep(5)


# perform_hover_operation()

def drag_and_drop():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    iframe_element = get_element(locator=(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
    driver.switch_to.frame(iframe_element)
    action = ActionChains(driver)

    image1 = get_element(locator=(By.XPATH, "//h5[text()='High Tatras']//parent::li"))
    trash_elem = get_element(locator=(By.ID, "trash"))
    action.drag_and_drop(image1, trash_elem)
    action.perform()
    time.sleep(5)

    image2 = get_element(locator=(By.XPATH, "//img[@src='images/high_tatras2_min.jpg']"))
    action.drag_and_drop(image2,trash_elem)
    action.perform()
    time.sleep(5)

    image3 = get_element(locator=(By.XPATH, "//img[@src='images/high_tatras3_min.jpg']"))
    action.drag_and_drop(image3, trash_elem)
    action.perform()
    time.sleep(5)

    image4 = get_element(locator=(By.XPATH, "//h5[text()='High Tatras 4']//parent::li"))
    action.drag_and_drop(image4,trash_elem)
    action.perform()
    time.sleep(5)


drag_and_drop()