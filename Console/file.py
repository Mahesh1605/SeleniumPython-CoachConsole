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
# ================================================================================================================#
# Creating a Tip for a District with BG Image URL and notification
# ================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()  # Events
driver.find_element(By.XPATH, "//a[@aria-label='Tips']").click()  # Tips
driver.find_element(By.XPATH, "//a[@ng-href='/tips/add']").click()  # Add New Tip
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='college']").click()  # College
time.sleep(2)
District = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in District:
    if CheckBox.text == "Beyond 12 District":
        CheckBox.click()
    if CheckBox.text == "Test District 2016":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()  # To close the pop-up