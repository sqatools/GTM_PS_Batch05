import

one_way_radio_btn = (By.XPATH, "//label[@for='search_type_option_ONEWAY']")
from_city = (By.XPATH, "//button[@data-ui-name='input_location_from_segment_0']")
close_default_selection = (By.CSS_SELECTOR, ".Icon-module__root___LRxqA.Tags-module__icon___Xf8q7")
from_airport_city = (By.XPATH, "//input[@placeholder='Airport or city']")
from_airport_city_selection = (By.XPATH, "//span[text()='Pune International Airport']")
dest_city = (By.XPATH, "//button[@data-ui-name='input_location_to_segment_0']")
to_airport_city = (By.XPATH, "//input[@placeholder='Airport or city']")
to_airport_city_selection = (By.XPATH, "//span[text()='Delhi International Airport']")
depart_date = (By.XPATH, "//button[@placeholder='Choose departure date']")
depart_date_selection = (By.XPATH, "//span[@data-date='2024-11-29']")
no_of_passengers = (By.XPATH, "//button[@data-ui-name='button_occupancy']")
no_of_adults_selection = (By.XPATH, "//button[@data-ui-name='button_occupancy_adults_plus']")
no_of_passengers_selection_done = (By.XPATH, "//button[@data-ui-name='button_occupancy_action_bar_done']")
search_button = (By.XPATH, "//button[@data-ui-name='button_search_submit']")

#######Applying filters#####
direct_only = (By.XPATH, "//div[text()='Direct only']")
air_india_express = (By.XPATH, "//input[@name='airlines-filter-IX']")
regional_air = (By.XPATH, "//input[@name='airlines-filter-QP']")

view_details = (By.XPATH, "(//span[text()='View details'])[1]")
select_flight = (By.XPATH, "//span[text()='Select']")
std_ticket = (By.XPATH, "//input[@value='standard']")
next_button = (By.XPATH, "//div[@data-testid='checkout_ticket_type_inner_next']")

traveler_details1 = (By.XPATH, "(//span[text()='Add this traveler’s details'])[1]")
first_name1 = (By.XPATH, "//input[contains(@name,'firstName')]")
last_name1 = (By.XPATH, "//input[contains(@name,'lastName')]")
gender_element1 = (By.XPATH, "//select[@name='passengers.0.gender']")
done_button1 = (By.XPATH, "//button[@data-testid='grouped_inputs_traveller_done_1']")

contact_details = (By.XPATH, "//input[@name='booker.email']")
phone_number = (By.XPATH, "//input[@aria-label='Phone number']")
next_button_details_page = (By.XPATH, "//span[text()='Next']")
next_button_travel_ins = (By.XPATH, "//span[text()='Next']")
skip_button = (By.XPATH, "//span[text()='Skip']")