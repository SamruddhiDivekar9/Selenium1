from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture()
def login():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait=WebDriverWait(driver,15)

    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys("Admin")
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys("admin123")
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
    

    yield
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    sleep(2)
    driver.find_element(By.LINK_TEXT,"Logout").click()
    sleep(2)
    driver.close()

def test_start1(login):
    driver1 = webdriver.Chrome()
    driver1.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("samruddhi")
    sleep(2)
    act=ActionChains(driver1)
    sleep(2)
    act.key_down(Keys.ENTER).perform()

def test_start2(login):
    driver2 = webdriver.Chrome()
    sleep(2)
    driver2.find_element(By.XPATH,"//span[text()='Admin']").click()