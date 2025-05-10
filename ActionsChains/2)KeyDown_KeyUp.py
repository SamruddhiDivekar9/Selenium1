from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://demowebshop.tricentis.com/')
sleep(2)

act=ActionChains(driver)
facebook=driver.find_element(By.XPATH,"//a[text()='Facebook']")
act.scroll_to_element(facebook).perform()

