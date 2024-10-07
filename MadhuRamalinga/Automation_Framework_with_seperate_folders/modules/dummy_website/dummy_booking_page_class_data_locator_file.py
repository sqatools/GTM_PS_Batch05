from selenium.webdriver.common.by import By

correct_option = (By.XPATH, "//div[@align='left']//li[1]/input")  #visa application
first_name = (By.XPATH, "(//input[@name='firstname'])[1]")
last_name = (By.XPATH, "(//input[@name='firstname'])[2]")
dob = (By.XPATH, "//input[@id='birthday']")
male_radio_button = (By.ID, "male")
no_of_passenger_dropdown = (By.ID, "admorepass")
round_trip = (By.ID, 'roundtrip')
from_city = (By.ID, 'fromcity')
dest_city = (By.ID, 'destcity')
dept_date = (By.CSS_SELECTOR, 'input[name="departdate"]')
return_date = (By.ID, 'returndate')
visa_interview = (By.ID, "visadate")
receive_ticket = (By.XPATH, "(//input[@type='radio'])[12]")  #Both option
billing_name = (By.ID, "billing_name")
phone = (By.ID, "billing_phone")
email = (By.ID, "billing_email")
address = (By.ID, "billing_address")
country_dropdown = (By.ID, "billing_country")
postcode = (By.ID, "postcode")
street_address = (By.ID, "street_address1")
most_visited_cities_radio_btn = (By.XPATH, "(//input[@type='checkbox'])[2]")  #Pune
