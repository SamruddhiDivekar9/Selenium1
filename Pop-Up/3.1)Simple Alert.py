# Alert msg which contains only one option ---->ok
#driver.switch_to.alert
#accept/dismiss/sendkeys/Text
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://demowebshop.tricentis.com/')
sleep(2)

driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()

alert=driver.switch_to.alert

print(alert.text)
sleep(2)

alert.accept()

"""
# ----------------------------------------------------------------------------------------------

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://demo.automationtesting.in/Alerts.html')
sleep(2)

driver.find_element(By.XPATH,"//a[contains(text(),'Alert with OK')]").click()
driver.find_element(By.XPATH,"//button[contains(text(), 'click the button to display an  alert box:' )]").click()
alert=driver.switch_to.alert

print(alert.text)
sleep(2)
alert.accept()

sleep(2)
driver.close()

