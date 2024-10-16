from selenium.webdriver.common.by import By

#1 new user registration
create_new_acc = (By.XPATH, "//p[@data-cy='LoginHeaderText']")
country_code_dd = (By.XPATH, "//p[@data-cy='MobileCodeDropDown_59']")
select_country_code = (By.XPATH, "(//span[text()='IN'])[2]")
sign_up_with_phno = (By.XPATH, "//input[@placeholder='Enter Mobile Number']")
continue_button1 = (By.XPATH, "//button[@data-cy='continueBtn']")
verify_and_create_acc = (By.XPATH, "//button[@data-cy='verifyAndCreate']")