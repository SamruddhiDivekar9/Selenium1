

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
driver.get('https://demoapps.qspiders.com/ui/frames?sublist=0')
sleep(2)
#
driver.switch_to.frame(0)
driver.find_element(By.ID,"username").send_keys("Samruddhi")
sleep(3)

driver.find_element(By.ID,"password").send_keys("7263068541")
sleep(2)

driver.find_element(By.ID,"submitButton").click()