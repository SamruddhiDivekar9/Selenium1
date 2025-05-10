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
sleep(4)
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
sleep(2)
album_3rd=driver.find_element(By.XPATH,"//a[text()='3rd Album']/../following-sibling::div[3]/div/span").text
print(album_3rd)
music_2=driver.find_element(By.XPATH,"(//a[text()='Music 2'])/../../div[3]/div/span").text
print(music_2)
music_2_2=driver.find_element(By.XPATH,"(//a[text()='Music 2'])[2]/../../div[3]/div/span").text
print(music_2_2)