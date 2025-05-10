
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

driver.find_element(By.XPATH,"//a[contains(text(),'Multiple iframe')]").click()

sleep(3)

first=driver.find_element(By.XPATH,"(//div[@class='w-1/2']/iframe)[1]")

driver.switch_to.frame(first)
sleep(3)

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("samruddhi7263@gamil.com")
sleep(1)

driver.find_element(By.XPATH,"//input[@id='password']").send_keys("samruddhi72")
sleep(1)

driver.find_element(By.XPATH,"//input[@id='confirm-password']").send_keys("samruddhi72")
sleep(1)

driver.find_element(By.XPATH,"//button[@id='submitButton']").click()
sleep(1)

driver.switch_to.parent_frame()

second=driver.find_element(By.XPATH,"(//div[@class='w-1/2']/iframe)[2]")
driver.switch_to.frame(second)

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("sam")
sleep(1)

driver.find_element(By.XPATH,"//input[@id='password']").send_keys("divekar")
sleep(1)

driver.find_element(By.XPATH,"//button[@id='submitButton']").click()
sleep(2)
