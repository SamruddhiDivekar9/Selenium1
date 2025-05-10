# Twitter
# take profile pic


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
opt.add_argument("--disable-notifications")

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
sleep(3)
dr.get('https://x.com/imro45?lang=en')
sleep(4)

tw=dr.find_element(By.XPATH,"//div[@aria-label='Home timeline']/div[3]/div/div/div/div/div/div/div/div/div[2]")
sleep(2)
tw.click()
# tw.screenshot("../screenshots/Rohit_Twitter.png")
twr=dr.find_element(By.XPATH,"//div[@id='react-root']/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/img")
sleep(2)
tw.screenshot("../screenshots/Rohit_Twitter_circle-1.png")
sleep(3)

dr.quit()