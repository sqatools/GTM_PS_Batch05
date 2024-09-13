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
radio_button1 = web_element(locator=(By.XPATH, "//div[@align='left']//li[1]/input")).click() # visa application
radio_button2 = web_element(locator=(By.XPATH, "//div[@align='left']//li[2]/input")).click() # return ticket
radio_button3 = web_element(locator=(By.XPATH, "//div[@align='left']//li[3]/input")).click() # hotel booking ticket
radio_button4 = web_element(locator=(By.XPATH, "//div[@align='left']//li[4]/input")).click() # hotel and flight booking
radio_button5 = web_element(locator=(By.XPATH, "//div[@align='left']//li[5]/input")).click() # Cab booking and return date

time.sleep(10)
first_name = web_element(locator=(By.XPATH, "(//input[@name='firstname'])[1]")).send_keys("Coco") # First Name
last_name = web_element(locator=(By.XPATH, "(//input[@name='firstname'])[2]")).send_keys("Melon") # Last Name
dob = web_element(locator=(By.CSS_SELECTOR, '#birthday')).send_keys("15/11/2023") # DOB
gender = web_element(locator=(By.ID, 'male')).click() #Gender
round_trip = web_element(locator=(By.ID, 'roundtrip')).click() #Round Trip
from_city = web_element(locator=(By.ID, 'fromcity')).send_keys("Kerala") # From City
dest_city = web_element(locator=(By.ID, 'destcity')).send_keys("Bangalore") # Destination City
dept_date = web_element(locator=(By.CSS_SELECTOR, 'input[name="departdate"]')).send_keys("10/09/2024") # Departure Date
return_date = web_element(locator=(By.ID, 'returndate')).send_keys("14/09/2024") # Return Date
visa = web_element(locator=(By.ID, "visadate")).send_keys("12/09/2024") # Visa Interview
receive_ticket = web_element(locator=(By.XPATH, "(//input[@type='radio'])[12]")).click() # Receive Ticket

time.sleep(10)
billing_name = web_element(locator=(By.ID, "billing_name")).send_keys("Coco") # Billing Name
billing_phone = web_element(locator=(By.ID, "billing_phone")).send_keys("7347989548") # Phone
email = web_element(locator=(By.ID, "billing_email")).send_keys("coco@gmail.com") # Email
address = web_element(locator=(By.ID, "billing_address")).send_keys("#16 HAL, Bangalore") # Address
#country = web_element(locator=(By.ID, "billing_country")).click() # Country
postcode = web_element(locator=(By.ID, "postcode")).send_keys("560017") # Postcode
street_address = web_element(locator=(By.ID, "street_address1")).send_keys("#16 HAL, Bangalore") # Address

time.sleep(10)
city_opt1 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[1]")).click() # Mumbai
city_opt2 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[2]")).click() # Pune
city_opt3 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[3]")).click() # Indore
city_opt4 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[4]")).click() # Kolkata
city_opt5 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[5]")).click() # Hyderabad
city_opt6 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[6]")).click() # Orangabad
city_opt7 = web_element(locator=(By.XPATH, "(//input[@type='checkbox'])[7]")).click() # Delhi

time.sleep(10)
driver.close()