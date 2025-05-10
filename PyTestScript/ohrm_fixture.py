import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[text()='Login']").click()

    yield
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()

def test_start1(login):
    driver = webdriver.Chrome()
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("samruddhi")
    act=ActionChains(driver)
    act.key_down(Keys.ENTER).perform()

def test_start2(login):
    driver = webdriver.Chrome()
    driver.find_element(By.XPATH,"//span[text()='Admin']").click()