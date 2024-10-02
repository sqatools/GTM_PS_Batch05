from selenium.webdriver.common.by import By

first_name_field = (By.XPATH, "(//input[@name='firstname'])[1]")
last_name_field = (By.XPATH, "(//input[@name='firstname'])[2]")
dob_calender = (By.XPATH, "//input[@id='birthday']")
male_radio_button = (By.ID, "male123")
num_passenger_dropdown = (By.ID, "admorepass")


