# 1)write a script for dws register form by using only css selector locators
import time
from time import sleep

# 2)write a script dws login page 1-open the browser 2-maximize 3-enter into dws page 4-click login link
# 5-verify login page by using web element 6-fill the details for login 7-click login 8-close the browser

# 1)
from selenium import webdriver
# expected_url='https://demowebshop.tricentis.com/'
#
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
# actual_url=driver.current_url
# print(actual_url)
# if expected_url==actual_url:
#     print('im in right page')
#     driver.find_element(By.CSS_SELECTOR,".ico-register").click()
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR,"#gender-female").click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR,"#FirstName").send_keys("samruddhi")
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR,"#LastName").send_keys("Divekar")
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("demo1@gmail.com")
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("Samruddhi@09")
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR,"input[name='ConfirmPassword']").send_keys("Samruddhi@09")
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR,"input[value='Register']").click()
#     time.sleep(3)
#
# else:
#     print('wrong page')
#
# driver.close()
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url='https://demowebshop.tricentis.com/'

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')
actual_url=driver.current_url
print(actual_url)
if expected_url==actual_url:
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'ico-login').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='Email']").send_keys("TeddyBear0907@gmail.com")
    sleep(1)
    driver.find_element(By.ID, 'Password').send_keys("Demo@123")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[value = 'Log in']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//div[@class  = 'header-menu']/ul/li[5]/a").click()
    sleep(1)
