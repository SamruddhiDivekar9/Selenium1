from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')

driver.find_element(By.XPATH, '//ul[@class="top-menu"]/li[5]/a').click()
sort = driver.find_element(By.XPATH, '//select[@id="products-orderby"]')
sel = Select(sort)
z = sel.options

for i in range(0, len(z)):
    sort = driver.find_element(By.XPATH, '//select[@id="products-orderby"]')
    sel = Select(sort)
    sel.select_by_index(i)
    sleep(2)

display = driver.find_element(By.XPATH, '//select[@name="products-pagesize"]')
sel1 = Select(display)
n = sel1.options

for j in range(len(n)):
    display = driver.find_element(By.XPATH, '//select[@name="products-pagesize"]')
    sel1 = Select(display)
    sel1.select_by_index(j)
    sleep(2)

view_as = driver.find_element(By.XPATH, '//select[@id="products-viewmode"]')
sel2 = Select(view_as)
p = sel2.options

for k in range(len(p)):
    view_as = driver.find_element(By.XPATH, '//select[@id="products-viewmode"]')
    sel2 = Select(view_as)
    sel2.select_by_index(k)
    sleep(2)

driver.close()