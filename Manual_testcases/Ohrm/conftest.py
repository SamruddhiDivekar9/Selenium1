from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup1(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def setup2(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,'//button[text()=" Login "]').click()
    request.cls.driver = driver
    yield
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    sleep(2)
    driver.find_element(By.LINK_TEXT,"Logout").click()
    sleep(5)
    driver.quit()

    