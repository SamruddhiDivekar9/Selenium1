from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://omayo.blogspot.com/')
sleep(2)

dropd=driver.find_element(By.XPATH,"//button[@class='dropbtn']")

# driver.execute_script("arguments[0].scrollIntoView(true)",dropd)    #------>true=webelement is in top/false=webelement is in bottom
# driver.execute_script("arguments[0].scrollIntoView(false)",dropd)