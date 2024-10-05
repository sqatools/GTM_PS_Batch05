from selenium.webdriver.common.by import By

#new user registration
new_customer = (By.ID, "nav-link-accountList-nav-line-1")
create_account = (By.ID, "createAccountSubmit")
name_field = (By.ID, "ap_customer_name")
email_id = (By.ID, "ap_email")
password_field = (By.XPATH, "(//input[@type='password'])[1]")
reenter_password = (By.ID, "ap_password_check")
verify_email = (By.CLASS_NAME, "a-button-input")

