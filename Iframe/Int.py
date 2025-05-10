from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://www.dream11.com/')
sleep(2)

driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@name='regEmail']").send_keys("7263068541")