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