
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
driver.get('https://demoapps.qspiders.com/ui/frames?sublist=0')
sleep(2)

driver.find_element(By.XPATH,"//a[contains(text(),'Nested with Multiple iframe')]").click()

sleep(2)

outermost=driver.find_element(By.XPATH,"//div[@class='px-8 pt-8 rounded-xl ']/iframe")
driver.switch_to.frame(outermost)
sleep(1)

outer=driver.find_element(By.XPATH,"//div[@class='form_container']/iframe")
driver.switch_to.frame(outer)
sleep(1)

email=driver.find_element(By.XPATH,"(//div[@class='form-group']/iframe)[1]")
sleep(1)
driver.switch_to.frame(email)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Admin@gmail.com")

driver.switch_to.parent_frame()
password=driver.find_element(By.XPATH,"(//div[@class='form-group']/iframe)[2]")
sleep(1)
driver.switch_to.frame(password)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Admin@1234")

driver.switch_to.parent_frame()
confpass=driver.find_element(By.XPATH,"(//div[@class='form-group']/iframe)[3]")
sleep(1)
driver.switch_to.frame(confpass)
driver.find_element(By.XPATH,"//input[@id='confirm']").send_keys("Admin@1234")

driver.switch_to.parent_frame()
submit=driver.find_element(By.XPATH,"(//div[@class='form-group']/iframe)[4]")
driver.switch_to.frame(submit)
sleep(1)
driver.find_element(By.XPATH,"//button[@id='submitButton']").click()


