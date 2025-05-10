# 2)dws digital download page-->open the br>maximize>enter into dws>verify by url>do login>click digital download webelement>
# >add all products which is present in digital download page by using find elements>remove the product which is having an higest price>
# >>>
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
expected_url="https://demowebshop.tricentis.com/"
actual_url=driver.current_url
if expected_url==actual_url:
    driver.find_element(By.CSS_SELECTOR, ".ico-login").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("TeddyBear0907@gmail.com")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Demo@123")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='RememberMe']").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
    sleep(1)
    add_to_cart=driver.find_elements(By.XPATH,"//input[@value='Add to cart']")

    for i in add_to_cart:
        i.click()
        sleep(2)

    driver.find_element(By.XPATH,"//span[text()='Shopping cart']").click()
    prices=driver.find_elements(By.XPATH,"//span[@class='product-unit-price']")

    high=0
    i=0
    count=1
    list=[]
    for price in prices:
        list.append(float(price.text))
        if high<list[i]:
            high=list[i]
            count=i+1
        i+=1


    # 1)FIRST_WAY----->
    driver.find_element(By.XPATH,"(//input[@name='removefromcart'])["+str(count)+"]").click()

    # 2)SECOND_WAY----->
    # checkbox=driver.find_elements(By.XPATH,"//input[@name='removefromcart']")
    # checkbox[count-1].click()

    driver.find_element(By.XPATH, "//input[@name='updatecart']").click()
    sleep(3)
    driver.close()

