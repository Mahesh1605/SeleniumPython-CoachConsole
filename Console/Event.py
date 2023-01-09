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
# Creating an Event for a District with notification
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='district']").click()
time.sleep(2)
District = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in District:
    if CheckBox.text  == "Anoka-Ramsey Community College District":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #To close the pop-up

driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break

driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys("Sample event")
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")
Iframe.send_keys(" sample event")
time.sleep(1)
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

#================================================================================================================#
# Creating an Event for a College with notification
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='college']").click()
time.sleep(2)
College = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in College:
    if CheckBox.text  == "Academy of Art Univ":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #To close the pop-up

driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break

driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys(" Sample event for a college")
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")
Iframe.send_keys(" Sample event")
time.sleep(1)
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

#================================================================================================================#
# Creating an Event for Term with notification
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='term']").click()
time.sleep(2)
Term = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in Term:
    if CheckBox.text  == "Quarter":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #To close the pop-up

driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break

driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys(" Sample event for a Term")
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")
Iframe.send_keys(" Sample event")
time.sleep(1)
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

#================================================================================================================#
# Creating an Event for Cohort with notification
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='cohort']").click()
time.sleep(2)
Cohort = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in Cohort:
    if CheckBox.text  == "12B - SPEAK cohort":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #To close the pop-up
driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break
driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys(" Sample event for a Cohort")
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")
Iframe.send_keys(" Sample event")
time.sleep(1)
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

#================================================================================================================#
# Creating an Event for Level with notification
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='level']").click()
time.sleep(2)
Cohort = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
for CheckBox in Cohort:
    if CheckBox.text  == "New":
        CheckBox.click()
        break
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #To close the pop-up
driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break
driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys(" Sample event for New Level")
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
Iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Area']")
Iframe.send_keys(" Sample event")
time.sleep(1)
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

#================================================================================================================#
# Create an Event with advanced recipient and plane text
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
driver.find_element(By.XPATH, "//a[@ng-href='/events/add']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-checkbox[@aria-label='Advanced Recipient Mode']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@aria-label='Recipient Group']").send_keys("district=150")
driver.find_element(By.XPATH, "//md-select[@name='content_owner']").click()
Content_Owner = driver.find_elements(By.XPATH, "//md-option[@ng-repeat='item in ctrl.results']")
for ContentOwner in Content_Owner:
    if ContentOwner.text == "Timbuktu College":
        ContentOwner.click()
        break
driver.find_element(By.XPATH, "//input[@aria-label='event title']").send_keys("Sample event")
Date = date.today().strftime("%b %d, %Y")
EventDate = driver.find_element(By.XPATH, "//input[@name='start_date']")
EventDate.click()
EventDate.clear()
EventDate.send_keys(Date)
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

#================================================================================================================#
# Clone an Event and save it without any changes
#================================================================================================================#
driver.find_element(By.XPATH, "//a[@aria-label='Events']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//md-select[@name='status']").click()
driver.find_element(By.XPATH, "//div[normalize-space()='Not Sent']").click()
#Status_NotSent = driver.find_elements(By.XPATH, "//div[@class='md-text ng-binding']")
#for Status in Status_NotSent:
#    if Status.text == "Not Sent":
#        Status.click()
#        break
time.sleep(3)
#Click on a Not Sent event
driver.find_element(By.XPATH, "(//small[@class='small-tag md-caption no-animate status ng-binding not_sent'])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='md-button md-ink-ripple']").click() #Click on Clone button
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Leave']").click() #Leave button
print(driver.title)
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()


#================================================================================================================#
#
#================================================================================================================#


