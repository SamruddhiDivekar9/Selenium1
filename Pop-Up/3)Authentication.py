from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get('https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/')
sleep(2)
