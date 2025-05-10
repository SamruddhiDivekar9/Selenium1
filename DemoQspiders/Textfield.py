from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.implicitly_wait(15)

first=driver.find_element(By.XPATH,"//li[contains(text(),'With placeholder')]")
second=driver.find_element(By.XPATH,"//li[contains(text(),'Without placeholder')]")
third=driver.find_element(By.XPATH,"//li[contains(text(),'With ToolTip')]")
fourth=driver.find_element(By.XPATH,"//li[contains(text(),'Multiline Text Area')]")
fifth=driver.find_element(By.XPATH,"//li[contains(text(),'Disabled')]")

list=[first,second,third,fourth,fifth]
for i in list:
    i.click()
    name = driver.find_element(By.XPATH, "//input[@id='name']")
    if name.is_displayed():
        name.send_keys("Samruddhi")
        sleep(1)
    else:
        ...

    email = driver.find_element(By.XPATH, "//input[@id='email']")
    if email.is_displayed():
        email.send_keys("samruddhidivekar@gmail.com")
        sleep(1)
    else:
        ...

    passw = driver.find_element(By.XPATH, "//input[@id='password']")
    if passw.is_displayed():
        passw.send_keys("sam@123")
        sleep(1)
    else:
        ...

    regbutton = driver.find_element(By.XPATH, "//button[@type='submit']")
    if regbutton.is_displayed():
        regbutton.click()
        sleep(4)
    else:
        ...

    email = driver.find_element(By.XPATH, "//input[@id='email']")
    if email.is_displayed():
        email.send_keys("samruddhidivekar@gmail.com")
        sleep(1)
    else:
        ...

    passw = driver.find_element(By.XPATH, "//input[@id='password']")
    if passw.is_displayed():
        passw.send_keys("sam@123")
        sleep(1)
    else:
        ...

    loginbutton = driver.find_element(By.XPATH, "//button[@type='submit']")
    if loginbutton.is_displayed():
        loginbutton.click()
        sleep(3)
    else:
        ...

    namet=driver.find_element(By.XPATH,"//textarea[@id='name']")
    if loginbutton.is_displayed():
        loginbutton.click()
        sleep(3)
    else:
        ...

    emailt = driver.find_element(By.XPATH, "//textarea[@id='email']")
    if loginbutton.is_displayed():
        loginbutton.click()
        sleep(3)
    else:
        ...

    passwt = driver.find_element(By.XPATH, "//textarea[@id='password']")
    if passwt.is_displayed():
        passwt.click()
        sleep(3)
    else:
        ...

    registet = driver.find_element(By.XPATH, "")
    if registet.is_displayed():
        registet.click()
        sleep(3)
    else:
        ...

    disable_name=driver.find_element(By.XPATH, "//input[@id='name']")
    driver.execute_script("arguments[0].value='Samruddhi'", disable_name)

    disable_email = driver.find_element(By.XPATH, "//input[@id='email']")
    driver.execute_script("arguments[0].value='samruddhidivekar@gmail.com'", disable_email)

    disable_passw = driver.find_element(By.XPATH, "//input[@id='passw']")
    driver.execute_script("arguments[0].value='sam@123'", disable_passw)


# name=driver.find_element(By.XPATH,"//input[@id='name']")
# name.send_keys("Samruddhi")
# sleep(1)
# email=driver.find_element(By.XPATH,"//input[@id='email']")
# email.send_keys("samruddhidivekar@gmail.com")
# sleep(1)
# passw=driver.find_element(By.XPATH,"//input[@id='password']")
# passw.send_keys("sam@123")
# sleep(1)
# regbutton=driver.find_element(By.XPATH,"//button[@type='submit']")
# regbutton.click()
# sleep(4)
#
# email=driver.find_element(By.XPATH,"//input[@id='email']")
# email.send_keys("samruddhidivekar@gmail.com")
# sleep(1)
# passw=driver.find_element(By.XPATH,"//input[@id='password']")
# passw.send_keys("sam@123")
# sleep(1)
# loginbutton=driver.find_element(By.XPATH,"//button[@type='submit']")
# loginbutton.click()
# sleep(3)
#
# driver.find_element(By.XPATH,"//li[contains(text(),'Without placeholder')]")
# sleep(1)
# name.click()
# name.send_keys("Samruddhi")
# sleep(1)
# email.click()
# email.send_keys("samruddhidivekar@gmail.com")
# sleep(1)
# passw.click()
# passw.send_keys("sam@123")
# sleep(1)
# regbutton.click()
# sleep(4)



