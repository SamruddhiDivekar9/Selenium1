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
else:
    print('wrong page')