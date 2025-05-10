"""
It represents hint element

anything which is present in  the webpage we call it as Webelement like radio button,
checkbox,Textfield,links etc

All these elements are developed by language like HTML, CSS , javascript and webelement present in htmldoc
for opening the it rightclick+inspect and ctrl+shift+i

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url='https://demowebshop.tricentis.com/'

driver=webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
vote=driver.find_element(By.ID,"vote-poll-1")
if vote.is_displayed():
    print("its a unique webelement")
else:
    print("im in wrong page")