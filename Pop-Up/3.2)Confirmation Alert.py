#alert msg which contains two option -----> ok and cancel

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://demo.automationtesting.in/Alerts.html')
sleep(2)

driver.find_element(By.XPATH,"(//a[contains(text(),'Alert with OK')])[2]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display a confirm box')]").click()
alert=driver.switch_to.alert

print(alert.text)
sleep(2)
alert.dismiss()
