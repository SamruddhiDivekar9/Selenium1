from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PageObjectModel.Loginpage import Login
from PageObjectModel.HomePage import Home
from PageObjectModel.AdminPage import Admin

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
act = ActionChains(driver)
driver.implicitly_wait(15)
exp_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
log=Login(driver)
home = Home(driver)
admin_page = Admin()
log.send_username("Admin")
log.send_password("admin123")
log.click_login()
act_url = driver.current_url
assert exp_url==act_url, "Login unsuccessful"
print("login successful")

home.click_admin()
admin_page.adda()
admin_page.user()
act.key_down(Keys.ARROW_DOWN).click().perform()
sleep(1)
dup = 'https://www.orangehrm.com/'
ax = driver.current_url
if ax == dup:
    sleep(2)
    driver.back()
sleep(1)
driver.back()
sleep(2)

admin_page.stat()
act.key_down(Keys.ARROW_DOWN).click().perform()
if dup == ax:
    sleep(1)
    driver.back()
sleep(1)
# dr.back()
sleep(1)

admin_page.emp()
sleep(1)

admin_page.send_emp('Monkey D. Luffy')
sleep(3)
assert dup == ax, 'i am not on admin_page page'
print('I am Admin page')
sleep(1)
act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
sleep(1)

admin_page.send_username('Gol.D.Asce')
sleep(1)

admin_page.send_password('Demo@0907')
sleep(2)

admin_page.send_conf_password('Demo@0907')
sleep(1)

admin_page.click_save()
sleep(5)

home.user_log()
sleep(1)

home.log_out()
sleep(3)

# dr.quit()
