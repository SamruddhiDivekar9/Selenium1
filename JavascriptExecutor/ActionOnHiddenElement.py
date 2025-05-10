from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(15)

driver.get('https://www.facebook.com/')
sleep(2)
driver.find_element(By.LINK_TEXT,"Create new account").click()
sleep(2)
hidden=driver.find_element(By.ID,"custom_gender")
driver.execute_script("arguments[0].click()",hidden)
driver.execute_script("arguments[0].value='Gay'",hidden)
