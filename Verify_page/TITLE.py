import time

from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_title='Royal Enfield India | Roadster, Adventure, Cruiser Motorcycles India'

driver=webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)
driver.get('https://www.royalenfield.com/in/en/home/')
actual_title=driver.title

if expected_title==actual_title:
    print("Correct page")
else:
    print("wrong page")
    time.sleep(4)
driver.close()