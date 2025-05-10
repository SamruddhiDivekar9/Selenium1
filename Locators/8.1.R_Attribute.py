# 1 march 2025

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,"//input[@class='search-box-text ui-autocomplete-input']").send_keys("samruddhi")
sleep(2)
driver.find_element(By.XPATH,"//input[@class='button-1 search-box-button']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Register']").click()

res=driver.find_element(By.XPATH,"//a[text()='Register']")

data=res.text
print(data)

comm=driver.find_element(By.XPATH,"//strong[text()='Community poll']")
c=comm.text
print(c)

driver.find_element(By.XPATH,"input[@name='NewsletterEmail']")