from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
sleep(2)

act=ActionChains(driver)
s1=driver.find_element(By.ID,"box6")
t1=driver.find_element(By.ID,"box106")
act.click_and_hold(s1).release(t1).perform()
sleep(2)

s2=driver.find_element(By.ID,"box7")
t2=driver.find_element(By.ID,"box107")
act.click_and_hold(s2).release(t2).perform()
sleep(2)

s3=driver.find_element(By.ID,"box1")
t3=driver.find_element(By.ID,"box101")
act.click_and_hold(s3).release(t3).perform()
sleep(2)

s4=driver.find_element(By.ID,"box4")
t4=driver.find_element(By.ID,"box104")
act.click_and_hold(s4).release(t4).perform()
sleep(2)

s5=driver.find_element(By.ID,"box5")
t5=driver.find_element(By.ID,"box105")
act.click_and_hold(s5).release(t5).perform()
sleep(2)

s6=driver.find_element(By.ID,"box2")
t6=driver.find_element(By.ID,"box102")
act.click_and_hold(s6).release(t6).perform()
sleep(2)

s7=driver.find_element(By.ID,"box3")
t7=driver.find_element(By.ID,"box103")
act.click_and_hold(s7).click(t7).perform()
sleep(5)

driver.close()