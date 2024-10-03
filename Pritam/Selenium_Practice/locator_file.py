from selenium.webdriver.common.by import By

first_name_locator = (By.XPATH, "(//input[@name='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@name='firstname'])[2]")
dob_calender = (By.ID, "birthday")
male_radio_btn = (By.ID, "male")

add_more_pass_dd = (By.ID, "admorepass")
one_way_radio = (By.ID, "oneway")
from_city_field = (By.ID, "fromcity")
dest_city_field = (By.ID, "destcity")
depart_date_calender = (By.ID, "departdate")
return_date_calender = (By.ID, "returndate")
