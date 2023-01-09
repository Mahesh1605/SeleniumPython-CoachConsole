import time
from datetime import date
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:\\Users\\ananthamahesh.yeruva\\Downloads\\chromedriver_win32\\chromedriver")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://console.horse.mycoachapp.org")
driver.maximize_window()
#================================================================================================================#
# Valid login
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("ananthamahesh.yeruva@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").send_keys("Letmein@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)  # Sleep command to enter 2FA code
driver.find_element(By.XPATH, "//span[@class='ng-scope']").click()
time.sleep(5)
print(driver.title)

#================================================================================================================#
# Creating a Tip for a District with BG Image and notification
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@aria-label='Tips']").click()
driver.find_element(By.XPATH,"//a[@ng-href='/tips/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@aria-label='title']").send_keys("Sample Tip Title")
driver.find_element(By.XPATH, "//textarea[@name='call_to_action']").send_keys("Sample Action Message")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.model.attribution']").send_keys("Hello Tip")

driver.find_element(By.XPATH, "//md-radio-button[@aria-label='Use background image']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@ng-model='ctrl.model.background.url']").send_keys("C:\\Users\\ananthamahesh.yeruva\\Downloads\\MyCoach_Mindmap.jpg")
Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")
Iframe.send_keys(" Sample Tip with Text")
time.sleep(2)
Date = date.today().strftime("%b %d, %Y")
TipDate = driver.find_element(By.XPATH, "//input[@name='date_to_send']")
TipDate.click()
TipDate.clear()
TipDate.send_keys(Date)
driver.find_element(By.XPATH, "//md-select[@aria-label='category']").click()
Category = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.mapping.flutterCategories']")
for category in Category:
    if category.text == "Career":
        category.click()
        break

driver.find_element(By.XPATH, "//button[@ng-click='ctrl.addReminder()']").click()
time.sleep(2)
Notification_Date = driver.find_element(By.XPATH, "//input[@name='reminder_0_date_to_send']")
Notification_Date.send_keys(Date)
driver.find_element(By.XPATH, "//textarea[@name='reminder_0_text']").send_keys("Text")
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
