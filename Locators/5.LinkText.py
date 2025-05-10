from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url='https://demowebshop.tricentis.com/'

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')

driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Shopping").click()