from time import sleep

import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from Fixture_POM.Loginpage import Login
from Fixture_POM.HomePage import Home

@pytest.fixture
def setup():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    login = Login(driver)
    home = Home(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.send_username("Admin")
    login.send_password("admin123")
    login.click_login()

    yield
    home.click_user()
    sleep(2)
    home.click_logout()
    sleep(5)
    driver.quit()


