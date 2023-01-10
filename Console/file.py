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
# Status filtering
# ================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()  # Events
driver.find_element(By.XPATH, "//a[@aria-label='Tips']").click()  # Tips
time.sleep(5)

#Calendar View
driver.find_element(By.XPATH, "//md-input-container[@class='flex-none hide show-gt-sm']//button[@aria-label='Calendar View'][normalize-space()='Calendar View']").click()
time.sleep(3)
