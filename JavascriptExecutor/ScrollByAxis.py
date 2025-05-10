from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://omayo.blogspot.com/')
sleep(2)

# driver.execute_script("window.scrollBy(0,1000)")
# sleep(2)
driver.execute_script("window.scrollBy(0,500)")

