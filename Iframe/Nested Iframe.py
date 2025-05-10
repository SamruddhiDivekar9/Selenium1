"""
One iframe inside another iframe is known as nested iframe
"""
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Frames.html')
sleep(2)

driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

iframe=driver.find_element(By.XPATH,"//div[@id='Multiple']/iframe")
driver.switch_to.frame(iframe)
sleep(2)

nested_iframe=driver.find_element(By.XPATH,"//div[@class='iframe-container']/iframe")
driver.switch_to.frame(nested_iframe)
sleep(2)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Samruddhi")

# driver.switch_to.parent_frame()
# driver.switch_to.parent_frame()

driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT,"Home").click()
sleep(5)

driver.close()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument('--disable-notifications')

dr = webdriver.Chrome(options=opt)

dr.maximize_window()

dr.get('https://demoapps.qspiders.com/ui/frames/nested?sublist=1')
sleep(1)
dr.switch_to.frame(0)
sleep(1)
dr.switch_to.frame(0)
sleep(1)
dr.find_element(By.ID, 'email').send_keys('Admin@gmail.com')
sleep(1)
dr.find_element(By.ID, 'password').send_keys('Admin@1234')
sleep(1)
dr.find_element(By.ID, "confirm-password").send_keys('Admin@1234')
sleep(1)
dr.find_element(By.ID, 'submitButton').click()
