
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url='https://demowebshop.tricentis.com/'

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')



# ---->IF CLASSNAME>'.CLASSNAMEVALUE' AND ID>'#IDVALUE'

driver.find_element(By.CSS_SELECTOR,"#small-searchterms").send_keys("samruddhi")
driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()