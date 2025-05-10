# 28_2_2025
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)


#for clicking every page
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[1]").click()
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[3]").click()
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[4]").click()
# sleep(4)


#register for a page using absolute xpath
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[1]").click()
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div[2]/input").click()
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/input").send_keys("samruddhi")
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/input").send_keys("Divekar")
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/input").send_keys("demo1@gmail.com")
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div/input").send_keys("Samruddhi@09")
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/input").send_keys("Samruddhi@09")
# sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[4]/input").click()
# sleep(4)

driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[2]").click()
sleep(2)