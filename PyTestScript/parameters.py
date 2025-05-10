import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username,password",[("Admin","admin123")])
def test_demo(username,password):
    print(username)
    print(password)

@pytest.mark.parametrize("user,passw",[("Admin","admin123")])
def test_orange_hrm(user,passw):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passw)

