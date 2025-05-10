
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.maximize_window()

tag=driver.find_elements(By.XPATH,"//input")
print(len(tag))


