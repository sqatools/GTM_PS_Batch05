import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
wait = WebDriverWait(driver, timeout=30)
time.sleep(10)
def web_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

sqa_tools = web_element(locator=(By.CSS_SELECTOR, '#Header1_headerimg')) # SQA Tools
print(sqa_tools.text)
dummy_website = web_element(locator=(By.CSS_SELECTOR, ".post-title.entry-title")) # Dummy Website
print(dummy_website.text)
website = web_element(locator=(By.XPATH, "//h1[contains(text(),'Booking')]")) # Booking Website
print(website.text)

time.sleep(10)
choose_option = web_element(locator=(By.XPATH, "//*[text()='Choose the correct option:']")) # Choose correct option
print(choose_option.text)
web_element(locator=(By.XPATH, "//div[@align='left']//li[1]/input")).click() # visa application
web_element(locator=(By.XPATH, "//div[@align='left']//li[2]/input")).click() # return ticket
web_element(locator=(By.XPATH, "//div[@align='left']//li[3]/input")).click() # hotel booking ticket
web_element(locator=(By.XPATH, "//div[@align='left']//li[4]/input")).click() # hotel and flight booking
web_element(locator=(By.XPATH, "//div[@align='left']//li[5]/input")).click() # Cab booking and return date

time.sleep(10)
web_element(locator=(By.XPATH, "(//input[@name='firstname'])[1]")).send_keys("Coco") # First Name
web_element(locator=(By.XPATH, "(//input[@name='firstname'])[2]")).send_keys("Melon") # Last Name
web_element(locator=(By.CSS_SELECTOR, '#birthday')).send_keys("15/11/2023") # DOB
web_element(locator=(By.ID, 'male')).click() #Gender
web_element(locator=(By.ID, 'roundtrip')).click() #Round Trip
web_element(locator=(By.ID, 'fromcity')).send_keys("Kerala") # From City
web_element(locator=(By.ID, 'destcity')).send_keys("Bangalore") # Destination City
web_element(locator=(By.CSS_SELECTOR, 'input[name="departdate"]')).send_keys("10/09/2024") # Departure Date
web_element(locator=(By.ID, 'returndate')).send_keys("14/09/2024") # Return Date
web_element(locator=(By.ID, "visadate")).send_keys("12/09/2024") # Visa Interview
web_element(locator=(By.XPATH, "(//input[@type='radio'])[12]")).click() # Receive Ticket

time.sleep(10)
web_element(locator=(By.ID, "billing_name")).send_keys("Coco") # Billing Name
web_element(locator=(By.ID, "billing_phone")).send_keys("7347989548") # Phone
web_element(locator=(By.ID, "billing_email")).send_keys("coco@gmail.com") # Email
web_element(locator=(By.ID, "billing_address")).send_keys("#16 HAL, Bangalore") # Address
#web_element(locator=(By.ID, "billing_country")).click() # Country
web_element(locator=(By.ID, "postcode")).send_keys("560017") # Postcode
web_element(locator=(By.ID, "street_address1")).send_keys("#16 HAL, Bangalore") # Address

time.sleep(10)
web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[1]")).click() # Mumbai

element = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[1]"))
element.click()

web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[2]")).click()
web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[3]")).click()
web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[4]")).click()
web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[5]")).click() # Hyderabad
web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[6]")).click() # Orangabad
web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[7]")).click() # Delhi



time.sleep(10)
driver.close()