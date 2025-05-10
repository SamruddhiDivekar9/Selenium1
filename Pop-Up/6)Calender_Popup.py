"""
we can handle as well as avoid



"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://www.easemytrip.com/')
sleep(2)
driver.find_element(By.ID,"ddate").click()
sleep(2)

driver.find_element(By.ID,"26/03/2025").click()
sleep(2)

driver.find_element(By.ID,"divRtnCal").click()
sleep(2)

while True:
    try:
        driver.find_element(By.ID,"frth_3_23/07/2025").click()
        break
    except:
        driver.find_element(By.ID,"img2Nex").click()
sleep(2)

















# for i in range(0,10):
#     if
# sleep(2)
#
# driver.find_element(By.ID,"rdate")
# sleep(2)
#
# driver.find_element(By.ID,"")
# sleep(2)
#
# driver.find_element(By.ID,"")
# sleep(2)
#
# driver.find_element(By.ID,"")
# sleep(2)