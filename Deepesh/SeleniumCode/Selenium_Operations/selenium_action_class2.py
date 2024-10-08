from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    for i in range(2, 5):
        image1 = get_element(locator=(By.XPATH, f"//h5[text()='High Tatras {i}']//parent::li"))
        action.drag_and_drop(image1, trash_elem)
        action.perform()
        time.sleep(3)


# drag_and_drop()


def scroll_to_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    contact_info_element = get_element(locator=(By.XPATH, "//h3[text()='Contact Info']"))
    action = ActionChains(driver)
    action.scroll_to_element(contact_info_element)
    # action.scroll_by_amount(100,200)
    # action.scroll_from_origin(300, 200) # Need to check
    action.perform()

    time.sleep(5)
    action.double_click(contact_info_element)
    action.perform()

    time.sleep(10)


# scroll_to_element()

import pyautogui
# pip install pyautogui

def context_click_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(5)
    about_link = get_element(locator=(By.XPATH, "//a[text()='About']"))
    action = ActionChains(driver)
    action.context_click(about_link)
    action.perform()
    time.sleep(2)
    pyautogui.press('up')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(10)


context_click_element()
