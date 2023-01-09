import time
from datetime import date
import date.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\\Users\\ananthamahesh.yeruva\\Downloads\\chromedriver_win32\\chromedriver")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://console.horse.mycoachapp.org")
driver.maximize_window()
# Valid login
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("murthy.upadhyayula@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").send_keys("Letmein@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)  # Sleep command to enter 2FA code
driver.find_element(By.XPATH, "//span[@class='ng-scope']").click()
time.sleep(5)
print(driver.title)

# Create an Event Clone an Event
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//md-select[@name='status']").click()
driver.find_element(By.XPATH, "//div[normalize-space()='Not Sent']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@md-virtual-repeat='item in ctrl'][2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Clone']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Leave']").click()
time.sleep(3)
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
Send_Date = driver.find_element(By.XPATH, "//input[@name='date_to_send']")
Send_Date.click()
Send_Date.clear()
Send_Date.send_keys(Date)
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()