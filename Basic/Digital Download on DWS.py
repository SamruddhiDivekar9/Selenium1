from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)

ex = 'https://demowebshop.tricentis.com/'

dr = webdriver.Chrome(options=op)
sleep(1)
dr.maximize_window()
sleep(1)
dr.get('https://demowebshop.tricentis.com/')
sleep(1)
ac = dr.current_url

if ex == ac:
    sleep(1)
    dr.find_element(By.CLASS_NAME, 'ico-login').click()
    sleep(1)
    dr.find_element(By.CSS_SELECTOR, "input[name='Email']").send_keys("TeddyBear090702@gmail.com")
    sleep(1)
    dr.find_element(By.ID, 'Password').send_keys("Demo@123")
    sleep(1)
    dr.find_element(By.CSS_SELECTOR, "input[value = 'Log in']").click()
    sleep(1)
    dr.find_element(By.XPATH, "//div[@class  = 'header-menu']/ul/li[5]/a").click()
    sleep(1)
    z = dr.find_elements(By.XPATH, "//input[@class='button-2 product-box-add-to-cart-button']")
    for i in z:
        i.click()
        sleep(3)

    dr.find_element(By.XPATH, "//span[text() = 'Shopping cart']").click()

    prices = dr.find_elements(By.XPATH, "//span[@class='product-unit-price']")



    l = []
    index=0
    high=0
    for price in prices:
        l.append(float(price.text))
        sleep(1)
    print(l)
    max = max(l)
    index = l.index(max)+1
    print(max, index)

    val = "//tr["+str(index)+"]/td[1]/input"
    print(val)

    dr.find_element(By.XPATH, val).click()
    sleep(3)
    dr.find_element(By.XPATH, '//input[@value="Update shopping cart"]').click()
