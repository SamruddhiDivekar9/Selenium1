"""
>write the script for facebook application
>open the br
>maximize>enter into fc login page
>click create new acc button
>fill all the details
>click signup
>close the browser
"""

from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from Basic.Find_Elements import driver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://www.facebook.com/")
sleep(2)

driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
sleep(1)


name=driver.find_element(By.XPATH, "//input[@aria-label='First name']")

name.click()
sleep(1)
name.send_keys("Samruddhi")
#
sleep(1)
surname=driver.find_element(By.XPATH, "//input[@name='lastname']")
surname.click()
sleep(1)
surname.send_keys("Divekar")
# sleep(2)
#
single=driver.find_element(By.XPATH,"//select[@id='day']")
s1=Select(single)
s1.select_by_index(8)
sleep(1)

single2=driver.find_element(By.XPATH,"//select[@id='month']")
s2=Select(single2)
s2.select_by_value("7")
sleep(1)

single3=driver.find_element(By.XPATH,"//select[@id='year']")
s3=Select(single3)
s3.select_by_visible_text("2002")
sleep(1)

driver.find_element(By.XPATH,"//label[contains(text(),'Female')]").click()

no=driver.find_element(By.XPATH, '//input[@name="reg_email__"]')

no.click()
no.send_keys("samruddhidivekar7263@gmail.com.")

password=driver.find_element(By.XPATH, '//input[@data-type="password"]')

password.click()
password.send_keys("Samruddhi@09")

signup=driver.find_element(By.XPATH, '//button[@name="websubmit"]')
signup.click()
sleep(10)

# driver.back()




# LOGIN

# login=driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy']")
# login.click()
# sleep(2)
# login.send_keys("demo@123")
#
# passw=driver.find_element(By.ID,"pass")
# passw.click()
# sleep(2)
# passw.send_keys("Samruddhi@09")
#
# driver.find_element(By.XPATH,"//button[@type='submit']").click()




# driver.close()