"""

WRITE A SCRIPT FOR OMAYO.BLOGSPOT
OPEN THE BROWSER
MAXIMIZE THE BR
ENTER INTO PAGE
CLICK THAT DROPDOWN ELEMENT
CLICK FACEBOOK
NAVIGATE BACK TO OMAYO.BLOGSPOT
CLICK TIMER ENABLED BUTTON
RETRIVE TEXT OF THE POPUP
HANDLE THE POPUP BY PRESSING OK BUTTON

--SHOULD NOT USE SLEEP--

"""
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
#
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=opt)
# driver.maximize_window()
#
# driver.implicitly_wait(15)
#
# driver.get("https://omayo.blogspot.com/")
#
# # act=ActionChains(driver)
# #
# # dropd=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
# # act.scroll_to_element(dropd)
#
# driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()
#
# driver.find_element(By.LINK_TEXT,"Facebook").click()
#
# driver.back()
#
# driver.find_element(By.XPATH,"//input[@id='timerButton']").click()


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.implicitly_wait(15)

driver.get("https://omayo.blogspot.com/")

driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()

driver.find_element(By.LINK_TEXT,"Facebook").click()

driver.back()
wait= WebDriverWait(driver, 15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='timerButton']")))
driver.find_element(By.XPATH,"//input[@id='timerButton']").click()

alert=driver.switch_to.alert

print(alert.text)
sleep(2)
alert.accept()


