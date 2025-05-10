from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://demowebshop.tricentis.com/')
sleep(2)

action=ActionChains(driver)

# for i in range(6):
#     action.key_down(Keys.TAB).perform()
#
# sleep(2)
# action.send_keys("Laptop").perform()
# sleep(2)
# action.key_down(Keys.ENTER).perform()



# OR
search_field=driver.find_element(By.ID,"small-searchterms")
action.send_keys_to_element(search_field,"Laptop").perform()
