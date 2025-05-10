# 1)open the br 2)maximize 3) enter dws page 4)verify the page using url 5)add 25$ virtual gift card
# 6)add to shopping cart
# fill all details and change the quantity to 2 , add the product to shopping cart ,verify the product wheather it is
# added succesfully inside shopping cart page, click checkbox and update---it will remove product ,close the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# from Basic.VerifyByUrl import actual_url

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

expected_url="https://demowebshop.tricentis.com/"
actual_url=driver.current_url
if expected_url==actual_url:
    driver.find_element(By.XPATH,"//a[text()='Digital downloads']").click()
    driver.find_element(By.XPATH,"//input[@class='button-2 product-box-add-to-cart-button']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientName']").send_keys("AngelPriya")
    sleep(1)
    driver.find_element(By.XPATH, "//input[@class='recipient-email']").send_keys("Beautiful@gmail.com")
    sleep(1)
    driver.find_element(By.XPATH, "//input[@class='sender-name']").send_keys("someone")
    sleep(1)
    driver.find_element(By.XPATH, "//input[@class='sender-email']").send_keys("demo2@gmail.com")
    sleep(1)
    driver.find_element(By.XPATH, "//textarea[@id='giftcard_2_Message']").send_keys("Thank You")
    sleep(2)
    cart_total=driver.find_element(By.XPATH, "//input[@id='addtocart_2_EnteredQuantity']")
    cart_total.clear()
    sleep(1)
    cart_total.send_keys("2")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@class='button-2 add-to-wishlist-button']").click()
    sleep(4)
    driver.find_element(By.XPATH,"//a[@class='ico-wishlist']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name='updatecart']").click()
    sleep(3)
    driver.close()