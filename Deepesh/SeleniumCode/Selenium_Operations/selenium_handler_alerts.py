from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

import time

browser = 'edge'
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

driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


def handle_alert_box():
    get_element(locator=(By.ID, "btnShowMsg")).click()
    alert1 = Alert(driver)
    print(alert1.text)
    time.sleep(5)
    alert1.accept()


# handler_alert_box()

def handle_confirm_box():
    get_element(locator=(By.ID, "button")).click()
    alert1 = Alert(driver)
    print(alert1.text)
    time.sleep(5)
    alert1.accept()
    para_element_ok = get_element(locator=(By.ID, 'demo'))
    print(para_element_ok.text)
    assert para_element_ok.text == 'You pressed OK!'

    get_element(locator=(By.ID, "button")).click()
    time.sleep(5)
    alert1.dismiss()
    para_element_cancel = get_element(locator=(By.ID, 'demo'))
    print(para_element_cancel.text)
    assert para_element_cancel.text == 'You pressed Cancel!'


#handle_confirm_box()


def handle_prompt_box(name):
    get_element(locator=(By.ID, "promptbtn")).click()
    alert1 = Alert(driver)
    print(alert1.text)
    alert1.send_keys(name)
    time.sleep(3)
    alert1.accept()
    prompt_msg = get_element(locator=(By.ID, "prompt"))
    print(prompt_msg.text)
    assert prompt_msg.text == f"Hello {name}! How are you today?"
    time.sleep(3)

handle_prompt_box("GTM")

time.sleep(5)
driver.close()
