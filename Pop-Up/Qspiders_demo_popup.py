from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)

driver.maximize_window()
sleep(2)

driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(2)

driver.find_element(By.XPATH,"//section[text()='Popups']").click()
sleep(1)

driver.find_element(By.XPATH,"//section[text()='Javascript']").click()
sleep(1)

driver.find_element(By.XPATH,"button[id='buttonAlert2']").click()
sleep(1)

alert=driver.switch_to.alert

alert.accept()
sleep(3)

driver.find_element(By.LINK_TEXT,"Confirm").click()
sleep(1)


driver.find_element(By.LINK_TEXT,"Prompt").click()
sleep(1)


