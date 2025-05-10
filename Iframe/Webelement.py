from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://www.dream11.com/')
sleep(2)
a=driver.find_element(By.ID,"send-sms-iframe")
driver.switch_to.frame(a)
driver.find_element(By.XPATH,"//input[@name='regEmail']").send_keys("7263068541")

#switch towards parent

driver.switch_to.parent_frame()
driver.find_element(By.ID,"hamburger").click()