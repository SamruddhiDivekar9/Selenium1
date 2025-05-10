from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)


# TO MAXIMIZE THE WINDOW
driver.maximize_window()

# ENTER INTO WEBPAGE QTALK
driver.get("https://chat.qspiders.com/")

# CLOSE THE BROWSERi
driver.close()

#22_assi_write script for 5 different webpages (bikes-KTM,royalenfield,kavasaki,honda,ducati)