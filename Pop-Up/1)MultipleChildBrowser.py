"""

TASK1---------------------------------


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('file:///C:/Users/Akash%20Divekar/Downloads/MultipleWindow%20(1).html')
sleep(2)

driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
sleep(3)
parent=driver.window_handles
print(parent)
driver.close()
for i in range(1,len(parent)):
    driver.switch_to.window(parent[i])
    driver.maximize_window()
    sleep(1)


# ----------------------------------------------------------------------------------------------------------------------------------

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('file:///C:/Users/Akash%20Divekar/Downloads/MultipleWindow%20(1).html')
sleep(2)

driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
sleep(3)
parent=driver.window_handles
print(parent)
driver.close()

olive='https://www.olivegarden.com/home'

for i in range(1,len(parent)):
    driver.switch_to.window(parent[i])
    if driver.current_url==olive:
        driver.maximize_window()
    else:
        driver.close()



# -----------------------------------------------------------------------------------------------------------------------------------
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get('file:///C:/Users/Akash%20Divekar/Downloads/MultipleWindow%20(1).html')
sleep(2)

driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
sleep(3)
parent=driver.window_handles
print(parent)

barb='https://www.barbequenation.com/'
olive='https://www.olivegarden.com/home'
giallo='https://www.giallozafferano.com/'

for i in range(1,len(parent)):
    driver.switch_to.window(parent[i])
    driver.maximize_window()
    sleep(1)

    if driver.current_url==barb:
        driver.find_element(By.XPATH,"//button[@aria-label='Open sidebar menu']").click()
        sleep(4)

    elif driver.current_url==olive:
        driver.find_element(By.ID, "onetrust-reject-all-handler").click()
        driver.find_element(By.XPATH,"//li[@id='header-login-link']/a").click()
        sleep(2)

    elif driver.current_url==giallo:
        driver.find_element(By.XPATH, "//button[contains(text(),'I Accept')]").click()
        driver.find_element(By.ID, "gz-header-hamburger").click()
        sleep(3)

    else:
        ...

#-----------------------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///C:/Users/rushi/Downloads/MultipleWindow%20(1).html")
c=driver.current_window_handle
driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
sleep(4)
child=driver.window_handles
# child.remove(c)
sleep(5)
print(child)
for i in child:
    driver.switch_to.window(i)
    # url = driver.current_url
    # print(url)
    if i !=c:
        cu=driver.current_url
        print(cu)

# -----------------------------------------------------------------------------------------------------------------------------------
"""