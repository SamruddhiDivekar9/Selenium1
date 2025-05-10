from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

ex = 'https://demowebshop.tricentis.com/'

driver = webdriver.Chrome(options=op)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get('https://demowebshop.tricentis.com/')
sleep(1)

date=datetime.now()
now=str(date).replace(":","-")
driver.save_screenshot(f"../Screenshots/DWS {now}.png")

sleep(3)
driver.close()