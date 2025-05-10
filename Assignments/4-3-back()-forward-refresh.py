#open br>maximize>enter into dws>enter into redbus> navigate dws>navigate to redbus>refresh page>close the browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
demo=driver.get("https://demowebshop.tricentis.com/")
sleep(2)
redbus=driver.get("https://www.redbus.in/")
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(3)
driver.close()