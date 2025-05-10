# enter into dws
# click register links
# fill all details
# click register button
# verify all
# after registering
# login
# with that data

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
dws_expected_url="https://demowebshop.tricentis.com/"
driver.get("https://demowebshop.tricentis.com/")
dws_actual_url=driver.current_url

assert dws_expected_url==dws_actual_url,"i am not in dws page"
print("i am in dws page")

reg_expected_url="https://demowebshop.tricentis.com/register"

register=driver.find_element(By.CLASS_NAME,"ico-register")
assert register.is_enabled()
print("register is enabled")
register.click()
reg_actual_url=driver.current_url

assert reg_expected_url==reg_actual_url,"i am not in register page"
print("i am in register page")


sleep(1)

male_radio=driver.find_element(By.ID,"gender-male")
assert male_radio.is_enabled(),"gender is not enabled"
print("gender is enabled")
male_radio.click()
assert male_radio.is_selected(),"gender is not selected"
print("gender is selected")

sleep(1)

first_name=driver.find_element(By.ID,"FirstName")
assert first_name.is_enabled(),"firstname text field is not enabled"
print("firstname textfield is enabled ")
first_name.send_keys("Hirtik")

sleep(1)

last_name=driver.find_element(By.ID,"LastName")
assert last_name.is_enabled(),"lastname text field is not enabled"
print("lastname textfield is enabled ")
last_name.send_keys("Roshan")

sleep(1)

Email=driver.find_element(By.ID,"Email")
assert Email.is_enabled(),"Email text field is not enabled"
print("Email textfield is enabled ")
random_number=random.randint(10,9999)
unique_mail=f"hroshan{random_number}@gmail.com"
print("unique_genrated_mail-->",unique_mail)
Email.send_keys(unique_mail)

sleep(1)

Password=driver.find_element(By.ID,"Password")
assert Password.is_enabled(),"Password text field is not enabled"
print("Password textfield is enabled ")
Password.send_keys("pass123")

sleep(1)

ConfirmPassword=driver.find_element(By.ID,"ConfirmPassword")
assert ConfirmPassword.is_enabled(),"ConfirmPassword text field is not enabled"
print("ConfirmPassword textfield is enabled ")
ConfirmPassword.send_keys("pass123")

sleep(1)

register_button=driver.find_element(By.ID,"register-button")
assert register_button.is_enabled(),"register-button text field is not enabled"
print("register-button textfield is enabled ")
register_button.click()

sleep(1)

register_confirm_button=driver.find_element(By.XPATH,"//input[@value='Continue']")
assert register_confirm_button.is_enabled(),"register_confirm_button text field is not enabled"
print("register_confirm_button textfield is enabled ")
register_confirm_button.click()

sleep(2)

driver.quit()
