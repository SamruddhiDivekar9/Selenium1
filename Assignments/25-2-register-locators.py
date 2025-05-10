import time
from time import sleep

# write script for dws page
# 1)open the br
# 2)maximize
# 3)enter into dws home pager
# 4)verify bu url
# 5)click register link
# 6)fill all details of register form
# 7)click register button
# 8)close the br


from selenium import webdriver
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
    print('im in right page')
    driver.find_element(By.CLASS_NAME,"ico-register").click()
    time.sleep(1)
    driver.find_element(By.ID,"gender-female").click()
    time.sleep(1)
    driver.find_element(By.NAME,"FirstName").send_keys("samruddhi")
    time.sleep(1)
    driver.find_element(By.ID,"LastName").send_keys("Divekar")
    time.sleep(1)+7+9
    driver.find_element(By.ID,"Email").send_keys("demo1@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"Password").send_keys("Samruddhi@09")
    time.sleep(1)
    driver.find_element(By.ID,"ConfirmPassword").send_keys("Samruddhi@09")
    time.sleep(2)
    driver.find_element(By.ID,"register-button").click()
    time.sleep(3)

else:
    print('wrong page')

driver.close()