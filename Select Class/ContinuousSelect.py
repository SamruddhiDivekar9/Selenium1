from time import sleep
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/Akash%20Divekar/Downloads/demo.html")
sleep(2)

single=driver.find_element(By.ID,"standard_cars")

sele=Select(single)

cars=sele.options

for i in range(0,len(cars)):
    sele.select_by_index(i)
    sleep(2)

driver.close()

