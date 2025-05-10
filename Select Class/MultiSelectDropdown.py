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

multi_select=driver.find_element(By.ID,"multiple_cars")
sel1=Select(multi_select)

sel1.select_by_visible_text("Audi")
sleep(1)
sel1.select_by_value("jgr")
sleep(1)
sel1.select_by_index(7)
sleep(1)

#Deselect
sel1.deselect_by_value("jgr")
sleep(1)
sel1.deselect_by_visible_text("Audi")
sleep(1)
sel1.deselect_by_index(7)
sleep(1)
sel1.deselect_all()



#options



