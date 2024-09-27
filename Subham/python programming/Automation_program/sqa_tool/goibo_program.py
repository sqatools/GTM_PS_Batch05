import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#explicit wait
from selenium.webdriver.support import expected_conditions as ec
#select dropdown
from selenium.webdriver.support.select import Select

browser = 'chrome'
driver = None

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()

driver.maximize_window()
wait = WebDriverWait(driver, timeout=30)

driver.get("https://www.goibibo.com")
print(driver.title)
time.sleep(5)


def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))


def get_element_list(locator):
    return wait.until(ec.visibility_of_all_elements_located(locator))


get_element(locator=(By.CSS_SELECTOR, "span[role='presentation']")).click()
logo = get_element(locator=(By.CSS_SELECTOR, "span[class='sc-1f95z5i-8 gnkTau header-sprite logo gi-logo']"))
print(logo.text)
bus_text = get_element(locator=(By.XPATH, "//h2[text()='Domestic and International Flights']"))
print(bus_text.text)
time.sleep(2)
get_element(locator=(By.XPATH, "//a[@href='/bus/']")).click()
time.sleep(2)
get_element(locator=(By.XPATH, "//input[@placeholder='Enter Source']")).send_keys("pune")
time.sleep(2)
get_element(locator=(By.XPATH, "//span[text()='Pune, Maharashtra']//parent::li")).click()
get_element(locator=(By.XPATH, "//input[@placeholder='Enter Destination']")).send_keys("mumbai")
time.sleep(2)
get_element(locator=(By.XPATH, "//span[text()='Mumbai, Maharashtra']//parent::li")).click()
get_element(locator=(By.XPATH, "//input[@data-testid='openCheckinCalendar']")).click()
time.sleep(2)
get_element(locator=(By.XPATH, "//span[text()='29']//parent::li")).click()
time.sleep(2)
get_element(locator=(By.XPATH, "//button[@data-testid='searchBusBtn']")).click()
time.sleep(2)
#update serach
update_serach = get_element(locator=(By.XPATH, "//span[text()='UPDATE SEARCH']"))
print(update_serach.text)
time.sleep(2)
#popular serach
popular_serach = get_element(locator=(By.XPATH, "//span[text()='Popular']"))
print(popular_serach)
time.sleep(2)
bus_type = get_element(locator=(By.XPATH, "//span[text()='Bus Type']"))
print(bus_type)
time.sleep(2)
get_element(locator=(By.XPATH, "(//div[text()='AC'])[2]")).click()
time.sleep(2)
get_element(locator=(By.XPATH, "(//div[text()='Sleeper'])[2]")).click()
time.sleep(2)
get_element(locator=(By.XPATH, "//span[@data-val='rating_high']")).click()
time.sleep(2)
#get_element(locator=(By.XPATH, "(//span[text()='SELECT SEAT'])[6]")).click()
all_elements = get_element_list(locator=(By.XPATH, "//p[text()='VRL Travels']//parent::div//parent::div//span[text()='SELECT SEAT']"))
all_elements[0].click()

time.sleep(2)
#Boarding Point

get_element(locator=(By.XPATH, "//p[contains(text(), 'Wakad Hinjwadi Bridge Under')]//ancestor::label//label")).click()
time.sleep(2)
#Dropping Point

time.sleep(2)
all_elements = get_element_list(locator=(By.XPATH, "//p[contains(text(), 'Kharghar')]//ancestor::label//label"))
#all_elements[0].click()
time.sleep(2)

#bus seat confrom
get_element(locator=(By.XPATH, "(//div[@class='SeatWithTooltipstyles__BusSleeper-sc-dkrka-1 kVBOmL'])[9]")).click()
time.sleep(2)
#continue page
get_element(locator=(By.XPATH, "//button[text()='CONTINUE']")).click()
time.sleep(2)


