import time

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
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("ananthamahesh.yeruva@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").send_keys("Letmein@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)  # Sleep command to enter 2FA code
driver.find_element(By.XPATH, "//span[@class='ng-scope']").click()
time.sleep(5)
print(driver.title)

# Create an Event with advanced recipient and plane text
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//md-select[@name='district']").click()
District = driver.find_elements(By.XPATH, "//div[@class='md-select-menu-container md-active md-clickable']")
for Select_districts in District:

    if Select_districts.text == "Apple Valley Test":
        Select_districts.click()
        print(Select_districts)
    break

