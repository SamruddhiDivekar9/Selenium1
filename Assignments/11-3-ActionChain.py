"""
1)Write a script for dws website
2)open the br
3)maximize th br
4)enter into dws page
5)click gift card section
6)add all products inside shopping cart
"""

from time import sleep
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)

driver.get('https://demowebshop.tricentis.com/')
sleep(2)

driver.find_element(By.XPATH,"(//a[contains(text(),'Gift Cards')])[1]").click()
cart=driver.find_elements(By.XPATH,"//div[@class='product-grid']/div/div/div[2]/div[3]/div[2]/input")

for i in cart:
    i.click()
    sleep(2)

    rname = driver.find_element(By.XPATH, "//input[@class='recipient-name']")
    remail = driver.find_element(By.XPATH, "//input[@class='recipient-email']")
    sname = driver.find_element(By.XPATH, "//input[@class='sender-name']")
    semail = driver.find_element(By.XPATH, "//input[@class='sender-email']")
    msg = driver.find_element(By.XPATH, "//textarea[@class='message']")
    add = driver.find_element(By.XPATH, "//input[@class='button-1 add-to-cart-button']")

    if rname:
        rname.send_keys("Mani Sir")
        sleep(1)
    else:
        ...
    if remail:
        remail.send_keys("manikandan@gmail.com")
        sleep(1)
    else:
        ...
    if sname:
        sname.send_keys("samruddhi")
        sleep(1)
    else:
        ...
    if semail:
        semail.send_keys("samruddhidivekar7263@gmail.com")
        sleep(1)
    else:
        ...
    if msg:
        msg.send_keys("Happy Holi")
        sleep(1)
    else:
        ...
    if add:
        add.click()
        sleep(1)
    else:
        ...
    driver.back()
    sleep(5)
driver.close()



