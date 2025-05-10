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

for i in range(2):
     action.key_down(Keys.TAB).perform()
action.key_down(Keys.ENTER).perform()

driver.find_element(By.ID,"gender-female").click()
sleep(3)


for i in range(1, 26):
    action.key_down(Keys.TAB).perform()

driver.find_element(By.ID,"gender-female").click()

action.key_down(Keys.TAB).send_keys('Teddy').perform()
sleep(2)
action.key_down(Keys.TAB).send_keys('Bear').perform()
sleep(2)
action.key_down(Keys.TAB).send_keys('Sorry@gmail.com').perform()
sleep(2)
action.key_down(Keys.TAB).send_keys('TeddyBear@0907').perform()
sleep(2)
action.key_down(Keys.TAB).send_keys('TeddyBear@0907').perform()
sleep(2)
action.key_down(Keys.TAB).key_down(Keys.ENTER).perform()


#
# tab=action.key_down(Keys.TAB).perform()
# for tab in range(32):
#     if tab==26:
#         action.send_keys("Samruddhi").perform()
#         sleep(2)
#     else:
#        ...
#     if tab==27:
#         action.send_keys("Divekar").perform()
#         sleep(2)
#     else:
#         ...
#     if tab==28:
#         action.send_keys("Samruddhidivekar7263@gmail.com").perform()
#         sleep(2)
#     else:
#         ...
#     if tab==29:
#         action.send_keys("Samruddhi@09").perform()
#         sleep(2)
#     else:
#         ...
#     if tab==30:
#         action.send_keys("Samruddhi@09").perform()
#         sleep(2)
#     else:
#         ...
#     if tab==31:
#         action.key_down(Keys.ENTER).perform()
#     else:
#         ...
# sleep(5)
#

