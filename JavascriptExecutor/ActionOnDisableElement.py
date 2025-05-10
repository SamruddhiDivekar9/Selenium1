from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(15)

driver.get('https://www.oracle.com/in/java/technologies/downloads/')
sleep(2)

jdk = driver.find_element(By.LINK_TEXT, 'jdk-17.0.14_linux-x64_bin.deb')

driver.execute_script("arguments[0].scrollIntoView(false)", jdk)
jdk.click()

disabled_button = driver.find_element(By.LINK_TEXT, 'Download jdk-17.0.14_linux-x64_bin.deb')

driver.execute_script("arguments[0].click()",disabled_button)
