
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
    search=driver.find_element(By.TAG_NAME,"input")
    search.send_keys("samruddhi")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"ico-register").click()
    time.sleep(2)
    driver.find_element(By.ID,value="small-searchterms").send_keys("laptop")
else:
    print('wrong page')