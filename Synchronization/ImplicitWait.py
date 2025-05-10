from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.implicitly_wait(15)
driver.get("https://www.shoppersstack.com/")

driver.find_element(By.ID,"loginBtn").click()

driver.find_element(By.XPATH,"//span[text()='Create Account']").click()