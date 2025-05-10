from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')
sleep(2)


parent=driver.current_window_handle
print(parent)    #-----> current window handle

action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()

driver.find_element(By.XPATH,"//a[text()='Facebook']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Twitter']").click()
sleep(2)

childs=driver.window_handles

# driver.switch_to.window(childs[1])
# sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Create new account']").click()
# sleep(2)
print(childs)

# driver.switch_to.window(childs[2])
# sleep(5)
# driver.find_element(By.XPATH,"//span[text()='Create account']").click()
# driver.close()
