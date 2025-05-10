
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
driver.get("https://demowebshop.tricentis.com/")
sleep(2)

driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
sleep(2)

single_sel=driver.find_element(By.ID,"products-orderby")
sele=Select(single_sel)

sort=sele.options

for i in range(0,len(sort)):
    single_sel = driver.find_element(By.ID, "products-orderby")
    sele = Select(single_sel)
    sele.select_by_index(i)
    sleep(2)

driver.close()