
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
sleep(3)
dr.get('https://www.instagram.com/rohitsharma45/?hl=en')
sleep(4)
# a.move_to_element()

dr.find_element(By.XPATH, '(//div[@role="dialog"]/div/div[2]/div/div/div/div)[1]').click()

img = dr.find_element(By.XPATH, '(//img[@crossorigin="anonymous"])[1]')
img.screenshot('Rohit.png')

sleep(3)
dr.quit()