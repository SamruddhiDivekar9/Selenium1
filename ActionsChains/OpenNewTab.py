from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)

driver.get('https://demowebshop.tricentis.com/')
sleep(2)

action=ActionChains(driver)
books=driver.find_element(By.XPATH,"//a[contains(text(),'Books')]")
action.key_down(Keys.CONTROL).click(books).perform()
action.key_up(Keys.CONTROL).perform()
sleep(2)


comp=driver.find_element(By.XPATH,"//a[contains(text(),'Computers')]")
action.key_down(Keys.SHIFT).click(comp).perform()

