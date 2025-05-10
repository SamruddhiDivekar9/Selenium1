from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Register.html")

action=ActionChains(driver)
name=driver.find_element(By.XPATH,'//input[@ng-model="FirstName"]')
action.send_keys_to_element(name,"samruddhi").perform()

surname=driver.find_element(By.XPATH,'//input[@ng-model="LastName"]')
action.send_keys_to_element(surname,"Divekar").perform()

address=driver.find_element(By.XPATH,'//textarea[@ng-model="Adress"]')
action.send_keys_to_element(address,"Pune").perform()

email=driver.find_element(By.XPATH,'//input[@ng-model="EmailAdress"]')
action.send_keys_to_element(email,"samruddhi@gmail.com").perform()

phone=driver.find_element(By.XPATH,'//input[@ng-model="Phone"]')
action.send_keys_to_element(phone,"7263068541").perform()

driver.find_element(By.XPATH,'//input[@value="FeMale"]').click()

driver.find_element(By.ID,"checkbox2").click()

language=driver.find_element(By.ID,"msdd").click()
# language.click()
sleep(3)
driver.find_element(By.XPATH,"//a[contains(text(),'English')]").click()
sleep(4)


butt=driver.find_element(By.ID,"footer")
action.key_down(butt).perform()

single_select=driver.find_element(By.ID,"Skills")
sel=Select(single_select)
sel.select_by_value("Python")

country=driver.find_element(By.ID,"country")
sel=Select(country)
sel.select_by_visible_text("India")

single_select3=driver.find_element(By.ID,"yearbox")
sel=Select(single_select3)
sel.select_by_visible_text("2002")

single_select4=driver.find_element(By.XPATH,"//select[@ng-model='monthbox']")
sel=Select(single_select4)
sel.select_by_visible_text("July")

single_select4=driver.find_element(By.ID,"daybox")
sel=Select(single_select4)
sel.select_by_visible_text("9")

passw=driver.find_element(By.ID,"firstpassword")
action.send_keys_to_element(passw,"Samruddhi@09").perform()

cpassw=driver.find_element(By.ID,"secondpassword")
action.send_keys_to_element(cpassw,"Samruddhi@09").perform()

driver.find_element(By.ID,"submitbtn").click()
