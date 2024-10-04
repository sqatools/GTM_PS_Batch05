from selenium.webdriver.common.by import By

one_way_radio_button = (By.XPATH, "//label[@for='search_type_option_ONEWAY']")
from_segment_button = (By.XPATH, "//button[@data-ui-name='input_location_from_segment_0']")
to_segment_button = (By.XPATH, "//button[@data-ui-name='input_location_to_segment_0']")
airport_city_input_field = (By.XPATH, "//input[@placeholder='Airport or city']")
from_city_airport_selection = (By.XPATH, "//span[text()='Chhatrapati Shivaji International Airport Mumbai']")
calender_locator = (By.XPATH, "//button[@placeholder='Choose departure date']")
calender_date = (By.XPATH, "//span[@data-date='2024-11-29']")
occupancy_of_passenger = (By.XPATH, "//button[@data-ui-name='button_occupancy']")
add_num_of_adults = (By.XPATH, "//div[@data-ui-name='occupancy_adults']//button[2]")
add_num_of_children = (By.XPATH, "//div[@data-ui-name='occupancy_children']//button[2]")
done_button = (By.XPATH, "//span[text()='Done']")
search_button = (By.XPATH, "//button[@data-ui-name='button_search_submit']")
cheapest_flight_section = (By.XPATH, "//button[@id='TAB-CHEAPEST']")
first_flight_view_details_btn = (By.XPATH, "//div[@id='flight-card-0']//button[@data-testid='flight_card_bound_select_flight']")
select_button = [By.XPATH, "//span[text()='Select']"]
standard_ticket_radio_btn = ["//div[text()='Standard ticket']"]
