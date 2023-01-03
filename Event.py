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
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("murthy.upadhyayula@zenq.com")
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
driver.find_element(By.XPATH, "//md-checkbox[@aria-label='Advanced Recipient Mode']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@aria-label='Recipient Group']").send_keys("district=150")
driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break
driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys("Sample event created using Selenium Web driver")
driver.find_element(By.XPATH, "//input[@aria-label='start date']").send_keys("Dec 4, 2022")
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Switch to plain text']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@ng-model='ctrl.model.text.formatted']").send_keys("Sample event")
driver.find_element(By.XPATH, "//md-select[@aria-label='category']").click()
Category = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.mapping.flutterCategories']")
for category in Category:
    if category.text == "Career":
        category.click()
        break
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()