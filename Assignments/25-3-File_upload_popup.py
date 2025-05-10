
"""
Write Script for naukari page
open browser
maximize the browser
enter into naukari page
click on register button
fill all the details
click on im experienced
upload resume
register now
"""

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
driver.get('https://www.naukri.com/')
sleep(2)

driver.find_element(By.ID,"register_Layer").click()
sleep(2)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Samruddhi")
sleep(2)

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("samruddhidivekar09@gmail.com")
sleep(2)


driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Samruddhi@09")
sleep(2)


driver.find_element(By.XPATH,"//input[@id='mobile']").send_keys("7263068541")
sleep(2)

bottom=driver.find_element(By.XPATH,"//a[contains(text(),'About Us')]")
a=ActionChains(driver)
a.scroll_to_element(bottom).perform()


driver.find_element(By.XPATH,"(//div[@class='iconWrap'])[1]").click()
sleep(2)

resume=driver.find_element(By.ID,"resumeUpload")
resume.send_keys("C:\\Users\Akash Divekar\\Downloads\\Samruddhi-Vijay-Divekar-FlowCV-Resume-20250302 (1).pdf")

sleep(2)

driver.find_element(By.XPATH,"//button[contains(text(),'Register now')]").click()
sleep(3)

# driver.close()


