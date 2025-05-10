from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(15)

driver.get('https://demoapps.qspiders.com/ui?scenario=1')
sleep(2)

driver.find_element(By.XPATH,"//li[contains(text(),'Disabled')]").click()
sleep(2)

name=driver.find_element(By.XPATH,"//input[@id='name']")

email=driver.find_element(By.XPATH,"//input[@id='email']")

passw=driver.find_element(By.XPATH,"//input[@id='password']")

driver.execute_script("arguments[0].value='Samruddhi'",name)
sleep(3)
driver.execute_script("arguments[0].value='samru@gmail.com'",email)
sleep(3)
driver.execute_script("arguments[0].value='Samruddhi@09'",passw)
sleep(4)

reg=driver.find_element(By.XPATH,'//button[@type="submit"]')

driver.execute_script("arguments[0].click()",reg)
