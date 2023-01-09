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
# Creating a Tip for a District with BG Image URL and notification
#================================================================================================================#

driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()      #Events

driver.find_element(By.XPATH, "//a[@aria-label='Tips']").click()        #Tips

driver.find_element(By.XPATH,"//a[@ng-href='/tips/add']").click()       #Add New Tip
time.sleep(2)

driver.find_element(By.XPATH, "//md-select[@name='district']").click()   #district
time.sleep(2)
District = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in District:
    if CheckBox.text  == "Test District 2016":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #To close the pop-up

driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()       #Content Owner
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break

driver.find_element(By.XPATH, "//input[@aria-label='title']").send_keys("Sample Tip For specific District")     #Title

driver.find_element(By.XPATH, "//textarea[@name='call_to_action']").send_keys("Sample Action Message")      #Action to call

driver.find_element(By.XPATH, "//input[@ng-model='ctrl.model.attribution']").send_keys("Hello Tip")     #attribute

driver.find_element(By.XPATH, "//md-radio-button[@aria-label='Use background image']").click()      #BG Image
time.sleep(2)
image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc_RuHxzAoTjHBJ4hpZoVexT0yyrh31NGW_TEAdhKz-g&s"
driver.find_element(By.XPATH, "//input[@ng-model='ctrl.model.background.url']").send_keys(image)

Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")     #Tip Details
Iframe.send_keys(" Sample Tip with Text")
time.sleep(1)

Date = date.today().strftime("%b %d, %Y")
TipDate = driver.find_element(By.XPATH, "//input[@name='date_to_send']")
TipDate.click()
TipDate.clear()
TipDate.send_keys(Date)

driver.find_element(By.XPATH, "//md-select[@aria-label='category']").click()        #Category
Category = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.mapping.flutterCategories']")
for category in Category:
    if category.text == "Career":
        category.click()
        break

driver.find_element(By.XPATH, "//button[@ng-click='ctrl.addReminder()']").click()       #Add New Notification
time.sleep(2)

Notification_Date = driver.find_element(By.XPATH, "//input[@name='reminder_0_date_to_send']")       #Date
Notification_Date.send_keys(Date)

driver.find_element(By.XPATH, "//textarea[@name='reminder_0_text']").send_keys("Text")      #Text

driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()     #Save