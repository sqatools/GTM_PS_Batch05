import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#explicit wait
from selenium.webdriver.support import expected_conditions as ec
#select dropdown
from selenium.webdriver.support.select import Select
browser = 'chrome'
driver = None

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()

driver.maximize_window()
wait = WebDriverWait(driver, timeout=30)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
print(driver.title)
header_element=driver.find_element(By.XPATH,"//h1[text()= ' Dummy Ticket Booking Website']")
print("Header name:",header_element.text)
driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()
driver.find_element(By.XPATH,"(//input[@id='firstname'])[1]").send_keys("SUBHAM")
driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]").send_keys("BEHERA")
driver.find_element(By.ID, "birthday").send_keys("09/15/2024")
driver.find_element(By.CSS_SELECTOR,"input[id='male']").click()
text1=driver.find_element(By.XPATH,"//h3[text()= ' Number of Additional Passangers']")
print(text1.text)
time.sleep(1)
element=driver.find_element(By.CSS_SELECTOR,"select[id='admorepass']")
drp=Select(element)
drp.select_by_index(2)
#travel details
text3=driver.find_element(By.XPATH,"//h2[@text()='Travel Details']")
print(text3.text)
driver.find_element(By.CSS_SELECTOR,"input[id='oneway']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='fromcity']").send_keys("mumbai")
driver.find_element(By.CSS_SELECTOR,"input[id='destcity']").send_keys("pune")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"input[id='departdate']").click()
driver.find_element(By.XPATH,"//input[@id='returndate']").click()
# How will you like to receive the dummy ticket(optional)
text4=driver.find_element(By.XPATH,"//b[contains(text(), 'How will you like to receive')]")  # xpath incorrect
print(text4.text)
driver.find_element(By.XPATH,"(//input[@id='female'])[1]").click()
text5=driver.find_element(By.XPATH,"//h2[text()='Billing Details']")
print(text5.text)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[id='billing_name']").send_keys("SUBHAM")
driver.find_element(By.CSS_SELECTOR,"input[id='billing_phone']").send_keys(7008619711)
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("subhambehera22@gmail.com")
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("pune")
element1=driver.find_element(By.CSS_SELECTOR,"select[id='billing_country']")
time.sleep(5)
drp=Select(element1)
drp.select_by_index(13)
driver.find_element(By.CSS_SELECTOR,"input[id='postcode']").send_keys(753001)
driver.find_element(By.CSS_SELECTOR,"input[id='Prefecture']").send_keys(753001)
#Most Visited Cities
text6=driver.find_element(By.XPATH,"//h2[text()='Most Visited Cities']")
print(text6.text)
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[7]").click()
text7=driver.find_element(By.XPATH,"(//h2[@class='title'])[1]")
print(text7.text)
driver.find_element(By.XPATH,"//input[@id='ContactForm2_contact-form-name']").send_keys("subham Behera")
driver.find_element(By.XPATH,"//input[@id='ContactForm2_contact-form-email']").send_keys("subhambehera22@gmail.com")
driver.find_element(By.XPATH,"(//textarea[@class='contact-form-email-message'])[1]").send_keys("thanku so much")
driver.find_element(By.CSS_SELECTOR,"input[id='ContactForm2_contact-form-submit']").click()

time.sleep(1)
driver.close()
















































