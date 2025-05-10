from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

ex = 'https://demowebshop.tricentis.com/'

driver = webdriver.Chrome(options=op)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get('https://demowebshop.tricentis.com/')
sleep(1)

driver.save_screenshot("DWS_home_page.png")
sleep(2)

logo=driver.find_element(By.XPATH,"//div[@class='header-logo']")
logo.screenshot("logo.png")
driver.quit()