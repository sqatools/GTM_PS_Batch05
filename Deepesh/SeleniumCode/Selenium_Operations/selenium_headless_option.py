from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options



import time

chrm_option = Options()
#chrm_option.add_argument('--headless')
driver = webdriver.Chrome(options=chrm_option)

driver.maximize_window()
# explicit wait
wait = WebDriverWait(driver, timeout=20)

driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


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
