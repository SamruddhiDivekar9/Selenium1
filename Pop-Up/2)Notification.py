# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
#
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option('detach', True)
#
# opt.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(options=opt)
# driver.maximize_window()
#
# driver.get('https://www.easemytrip.com/')
# sleep(2)

# action=ActionChains(driver)
# action.key_down(Keys.TAB).click().perform()
# action.key_up(Keys.TAB).perform()
# sleep(2)
# action.key_down(Keys.ENTER).click().perform()



# --------------------------------------------------------------------

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://www.agoda.com/')
sleep(2)

