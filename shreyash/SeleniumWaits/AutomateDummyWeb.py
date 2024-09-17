from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

wait = WebDriverWait(driver,timeout=20)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

def get_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

element=driver.find_element(By.XPATH,"//h3[@class='post-title entry-title']")
print("Check element is is displayed:",element.is_displayed())

element=driver.find_element(By.XPATH,"//h1[text()=' Dummy Ticket Booking Website']")
print("Check element is is displayed:",element.is_displayed())

element=driver.find_element(By.XPATH,"//h3[text()='Choose the correct option:']")
print("Check element is is displayed:",element.is_displayed())

driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()

element=driver.find_element(By.XPATH,"//h2[text()='Passenger Details']")
print("check element is displayed:", element.is_displayed())

firstname_element=driver.find_element(By.XPATH,"(//input[@id='firstname'])[1]").send_keys("Shreyas")
time.sleep(3)
lasttname_element=driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]").send_keys("Bhokare")
time.sleep(3)
date_of_birth = driver.find_element(By.ID,"birthday").send_keys("05/09/1991")
time.sleep(3)
male_element=driver.find_element(By.XPATH,"(//input[@type='radio'])[6]").click()
time.sleep(3)

element=driver.find_element(By.XPATH,"//*[text()=' Number of Additional Passangers'] ")
print("Check element is is displayed:",element.is_displayed())

pass_element= get_element(locator=(By.ID,"admorepass"))
select_obj= Select(pass_element)
select_obj.select_by_index("2")
time.sleep(3)

element=driver.find_element(By.XPATH,"//h2[text()=' Travel Details ']")
print("check element is displayed:", element.is_displayed())

driver.find_element(By.XPATH,"(//input[@type='radio'])[9]").click()
time.sleep(3)

fromcity_element=driver.find_element(By.ID,"fromcity").send_keys("Mumbai")
Dest_city_element=driver.find_element(By.ID,"destcity").send_keys("Pune")
time.sleep(3)
Dest_city_element=driver.find_element(By.ID,"destcity").clear()
Dest_city_element=driver.find_element(By.ID,"destcity").send_keys("Chennai")
time.sleep(3)

depart_date = driver.find_element(By.ID,"departdate").send_keys("09/12/2024")
time.sleep(2)
return_date = driver.find_element(By.ID,"returndate").send_keys("13/12/2024")
time.sleep(2)

Deliver_element=driver.find_element(By.XPATH,"//h2[text()='Delivery Option']")
print("check element is displayed:", element.is_displayed())

visa_date=driver.find_element(By.ID,"visadate").send_keys("08/12/2024")
time.sleep(2)

rcv_tkt_element=driver.find_element(By.XPATH,"//b[text()='How will you like to receive the dummy "
                                             "ticket(optional)']")
print("check element is displayed:", element.is_displayed())

whats_element=driver.find_element(By.XPATH,"(//input[@type='radio'])[11]").click()
time.sleep(2)

Billing_det_element=driver.find_element(By.XPATH,"//h2[text()='Billing Details']")
print("check element is displayed:", element.is_displayed())

Bill_name_element=driver.find_element(By.XPATH,"//input[contains(@id,'billing_name')]").send_keys("Shreyas Bhokare")
time.sleep(2)

Phone_no_element=driver.find_element(By.XPATH,"//input[contains(@id,'billing_phone')]").send_keys("8698697807")
time.sleep(2)

Bill_email_element=driver.find_element(By.XPATH,"//input[contains(@id,'billing_email')]").send_keys("shre@gmail.com")
time.sleep(2)

Stree_add_element=driver.find_element(By.XPATH,"//input[contains(@id,'billing_address')]").send_keys("3rd lane,Noida")
time.sleep(2)

country_element= get_element(locator=(By.ID,"billing_country"))
select_obj2= Select(country_element)
select_obj2.select_by_index("12")
time.sleep(2)

post_cd_element=driver.find_element(By.XPATH,"//input[contains(@name,'postcode')]").send_keys("201307")
time.sleep(2)

prefacture_element=driver.find_element(By.XPATH,"//input[contains(@name,'prefecture')]").send_keys("Government")
time.sleep(2)

Street_add1_element=driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys("Block-C")
time.sleep(2)

Street_add2_element=driver.find_element(By.XPATH,"//input[@id='street_address2']").send_keys("RWA colony")
time.sleep(2)

Most_vst_ct_element=driver.find_element(By.XPATH,"//h2[text()='Most Visited Cities']")
print("check element is displayed:", element.is_displayed())

checkbox_element=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1] ").click()
checkbox_element=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2] ").click()
checkbox_element=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[7] ").click()
time.sleep(2)

driver.close()

