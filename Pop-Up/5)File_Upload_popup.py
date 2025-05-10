"""
we can able to handle as well as avoid

AVOID--->
we can avoid using sendkeys
element should be under input tag
if it not present under input tag then we cant avoid it
locate the element by using Xpath


HANDLE--->

pynput

"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://www.ilovepdf.com/word_to_pdf')
sleep(2)

file=driver.find_element(By.XPATH,"//input[@type='file']")
file.send_keys("C:\\Users\\Akash Divekar\\Downloads\\selenium notes.docx")

