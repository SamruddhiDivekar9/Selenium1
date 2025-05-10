# write sc for dws page>open br>maximize the br>enter into dws page>verify by title>click excellent radio button
# >good radio button>Poor >very bad>Try with for loop
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
if expected_title==actual_title:
    a=driver.find_element(By.XPATH,"//input[@id='pollanswers-1']")
    b=driver.find_element(By.ID,"pollanswers-2")
    c=driver.find_element(By.XPATH, "//label[text()='Poor']")
    d=driver.find_element(By.XPATH,"//label[text()='Very bad']")
    def a_click():
        x=[a,b,c,d]
        for i in x:
            i.click()
            sleep(1)
    a_click()
    print("Clicked on all radio buttons")
driver.close()