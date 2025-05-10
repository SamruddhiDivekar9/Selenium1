from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.maximize_window()
expected_title="Demo Web Shop"
actual_title=driver.title

community_poll=driver.find_elements(By.XPATH,"//input[@type='radio']")


# for poll in community_poll:
#     poll.click()
#     sleep(1)

# poll=0
# while poll<len(community_poll):
#     community_poll[poll].click()
#     sleep(1)
#     poll+=1

links=driver.find_elements(By.XPATH,"//div[@class='header-links']/ul/li/a")
print(links)

for l in links:
    l.click()
    sleep(2)
    driver.back()
driver.close()

