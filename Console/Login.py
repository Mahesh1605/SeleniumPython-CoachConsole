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

#================================================================================================================#
#Invalid login with valid username and invalid password
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("ananthamahesh.yeruva@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").send_keys("Letmein")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//md-card-content[@class='ng-binding']").text
print(message)
driver.refresh()

#================================================================================================================#
#Invalid login with invalid username and valid password
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("ananthamahesh@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").send_keys("Letmein@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//md-card-content[@class='ng-binding']").text
print(message)
driver.refresh()

#================================================================================================================#
#Empty username and valid password
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//div[@class='md-input-messages-animation md-auto-hide ng-active']").text
print(message)
driver.refresh()

#================================================================================================================#
#Valid username and empty password
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("ananthamahesh.yeruva@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//div[contains(text(),'This is required')]").text
print(message)
driver.refresh()

#================================================================================================================#
#not an username
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("not an email")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//div[@class='md-input-messages-animation md-auto-hide ng-active']").text
print(message)
driver.refresh()

#================================================================================================================#
#forgot password with valid email
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@ui-sref='guest.forgotpass']").click()
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ananthamahesh.yeruva@zenq.com")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//p[@class='md-padding']").text
print(message)
driver.find_element(By.XPATH, "//a[@ui-sref='guest.login']").click() #Back to Login button
driver.refresh()

#================================================================================================================#
#forgot password with valid email
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@ui-sref='guest.forgotpass']").click()
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("mail@gmail.com")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.XPATH, "//md-toast[@class='ng-scope _md md-bottom md-left']").text
print(message)
driver.find_element(By.XPATH, "//a[@ui-sref='guest.login']").click()
driver.refresh()

#================================================================================================================#
#Valid login
#================================================================================================================#
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.email']").send_keys("ananthamahesh.yeruva@zenq.com")
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.password']").send_keys("Letmein@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)
driver.find_element(By.XPATH, "//span[@class='ng-scope']").click()
time.sleep(5)