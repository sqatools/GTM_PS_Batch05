from selenium.webdriver.common.by import By

#1 new user registration
new_customer = (By.ID, "nav-link-accountList-nav-line-1")
create_account = (By.ID, "createAccountSubmit")
name_field = (By.ID, "ap_customer_name")
email_id = (By.ID, "ap_email")
password_field = (By.XPATH, "(//input[@type='password'])[1]")
reenter_password = (By.ID, "ap_password_check")
verify_email = (By.CLASS_NAME, "a-button-input")

#2 & 3 verify login is successful with correct email and password or fails with incorrect credentials
existing_customer = (By.ID, "nav-link-accountList-nav-line-1")
existing_cust_email = (By.ID, "ap_email")
continue_button = (By.ID, "continue")
existing_cust_password = (By.ID, "ap_password")
sign_in_button = (By.ID, "signInSubmit")

#4 edit profile information
account_lists = (By.ID, "nav-link-accountList")
your_addresses = (By.XPATH, "//span[contains(text(),'Edit, remove')]")





#5 searching for products
search_amazon1 = (By.ID, "twotabsearchtextbox")
search_entered_product1 = (By.ID, "nav-search-submit-button")

#6 & 7 searching with filters
filter_by_prime = (By.XPATH, "//i[@aria-label='Prime Eligible']")
filter_by_review = (By.XPATH, "//div[@aria-label='4 Stars & Up']")
filter_by_brands = (By.XPATH, "(//span[@role='button'])[2]")
filter_by_brands_options = (By.XPATH, "//span[text()='Ruffwear']")

#8 sorting
sort_by = (By.XPATH, "//span[text()='Sort by']")
sort_by_price = (By.ID, "s-result-sort-select_1")

#9 & 10 adding to cart and removing
selected_product1 = (By.XPATH, "//span[contains(text(),'Boot Socks')]")
quantity = (By.ID, "a-autoid-1-announce")
add_quantity = (By.ID, "quantity_1")
add_to_cart1 = (By.ID, "add-to-cart-button")

search_amazon2 = (By.ID, "twotabsearchtextbox")
search_entered_product2 = (By.ID, "nav-search-submit-button")
selected_product2 = (By.XPATH, "(//span[contains(text(),'Benebone Medium')])[1]")
add_to_cart2 = (By.ID, "add-to-cart-button")
go_to_cart = (By.ID, "nav-cart-count-container")
remove_item = (By.XPATH, "(//input[@data-action='delete'])[1]")
















