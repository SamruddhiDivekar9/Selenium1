# 1)
# write script for facebook application
# open the br
# maximize br
# enter into facebook login page
# after that verify the page by using url
# close the br

# 2)
# write script for redbus application
# open the br
# maximize br
# enter into redbus login page
# after that verify the page by using title
# close the br

# condition: Dont do copy paste

from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url='https://www.royalenfield.com/in/en/home/'

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.royalenfield.com/in/en/home/')
actual_url=driver.current_url
print(actual_url)
if expected_url==actual_url:
    print('im in right page')
else:
    print('wrong page')
driver.close()


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
