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
    follow=driver.find_elements(By.XPATH, "//div[@class='column follow-us']/ul/li/a")
    for i in follow:
        # a=driver.find_element(By.XPATH, "//div[@class='column follow-us']/ul/li[{i}]")
        i.click()
        sleep(2)
        if driver.current_url=="https://demowebshop.tricentis.com/news/rss/1":
            driver.back()

driver.close()
