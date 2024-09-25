import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.goibibo.com/")
wait = WebDriverWait(driver, timeout=30)
time.sleep(5)


def web_element(locator):
    return wait.until(ec.visibility_of_element_located(locator))

#Bus Booking
web_element(locator=(By.XPATH, "//span[@role='presentation']")).click() #pop-up close
web_element(locator=(By.LINK_TEXT, "Bus")).click() #Bus ticket booking
web_element(locator=(By.NAME, "autosuggestBusSRPSrcHomeName")).send_keys("Bangalore") #From
web_element(locator=(By.XPATH, "//span[text()='Bangalore, Karnataka']")).click() #Select Banaglore
web_element(locator=(By.ID, "autosuggestBusSRPDestHome")).send_keys("Delhi") #To
web_element(locator=(By.XPATH, "//span[text()='Delhi']")).click() #Select Delhi
web_element(locator=(By.XPATH, "//input[@data-testid='openCheckinCalendar']")).click() #Travel Date
web_element(locator=(By.CSS_SELECTOR, ".ArrowRightIcon-sc-t9vcrx-0.dBEphc")).click() #Select right click for next month
web_element(locator=(By.XPATH, "//span[text()='14']")).click() #Select date
web_element(locator=(By.XPATH, "//button[@data-testid='searchBusBtn']")).click() #Search Bus

#Bus selection by filter
web_element(locator=(By.XPATH, "(//div[text()='AC'])[1]")).click() #Filter AC in Popular
web_element(locator=(By.XPATH, "(//div[text()='Sleeper'])[2]")).click() #Filter Sleeper in Bus Type
time.sleep(2)
web_element(locator=(By.XPATH, "(//div[contains(text(),'midnight')])[2]")).click() #Filter departure time
time.sleep(2)
web_element(locator=(By.XPATH, "//a[contains(text(),'boarding')]")).click() #Show all boarding points
time.sleep(2)
web_element(locator=(By.XPATH, "//span[@title='Bhawani HotelNear dobbaspet']")).click() #Radio button - Bhawani
time.sleep(2)
web_element(locator=(By.XPATH, "//span[text()='Mahadev Travels']")).click() #Select Operator - Mahadev Circle
time.sleep(2)
#Select Amenities
web_element(locator=(By.XPATH, "//a[@data-val='amenities']")).click() #Show all Amenities
#time.sleep(2)
web_element(locator=(By.XPATH, "//span[@title='Water Bottle']")).click() #Water Bottle
time.sleep(2)
web_element(locator=(By.XPATH, "(//span[text()='Blankets'])[1]")).click() #Blankets
time.sleep(2)
web_element(locator=(By.XPATH, "//span[@title='USB port for charger']")).click() #USB port
time.sleep(2)
#web_element(locator=(By.XPATH,"//span[@title='Bed Sheet']")).click() #Bed Sheet
#time.sleep(2)
web_element(locator=(By.XPATH, "//span[@title='WIFI']")).click() #WiFi
time.sleep(2)
#web_element(locator=(By.XPATH, "//span[text()='CCTV']")).click() #CCTV
#time.sleep(2)

#Seat selection
web_element(locator=(By.XPATH, "(//span[text()='SELECT SEAT'])[1]")).click() #Select Seat
time.sleep(2)

#Scroll and Select boarding point - 22:50
def scroll_operation():
    action = ActionChains(driver)
    boarding_point = web_element(locator=(By.XPATH, "//p[text()='Boarding Point']//following-sibling::div//label[8]"))
    action.move_to_element(boarding_point).click()
    action.perform()
scroll_operation()

time.sleep(2)
web_element(locator=(By.XPATH, "//p[text()='Dropping Point']//following-sibling::div//label[2]")).click() #Select dropping point
time.sleep(2)
web_element(locator=(By.XPATH, "(//*[@fill='#FFF'])[2]")).click() #Select seat
time.sleep(2)
web_element(locator=(By.XPATH, "//button[text()='CONTINUE']")).click() #Continue
time.sleep(2)

#Traveller details
web_element(locator=(By.ID, "insuranceNo")).click() #Insurance
web_element(locator=(By.XPATH, "//input[@placeholder='Enter Full Name']")).send_keys("Coco") #Full Name
time.sleep(2)
web_element(locator=(By.XPATH, "//input[@placeholder='Age']")).send_keys(18) #Age
web_element(locator=(By.XPATH, "//*[text()='Male']")).click() #Gender
time.sleep(2)
web_element(locator=(By.XPATH, "//input[@placeholder='Enter Email Address']")).send_keys("coco@gmail.com") #Email ID
web_element(locator=(By.XPATH, "//input[@placeholder='Enter Mobile Number']")).send_keys(7337879327) #Ph No.
time.sleep(2)
web_element(locator=(By.ID, "Billing Address")).send_keys("HAL Old Airport Road, Bangalore") #Address
web_element(locator=(By.ID, "Pincode")).send_keys(560017) #Pincode
time.sleep(2)

dd_element = web_element(locator=(By.XPATH, "//label[text()='State']"))
dd_element.click()
#select_obj = Select(dd_element)
#select_obj.select_by_visible_text("Karnataka")
time.sleep(3)

def scroll_to_element():
    action1 = ActionChains(driver)
    state = web_element(locator=(By.XPATH, "//li[text()='Karnataka']"))
    action1.move_to_element(state).click()
    action1.perform()
scroll_to_element()

time.sleep(2)
#web_element(locator=(By.ID, "confirm_check")).click() #Save billing details
web_element(locator=(By.XPATH, "//button[contains(text(),'Pay')]")).click() #Pay

time.sleep(5)
driver.close()
