import pytest
from selenium import webdriver
from time import sleep
from selenium .webdriver.common.by import By

@pytest.mark.usefixtures("setup1")
class TestCase1:
    def test_001(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_002(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admina")
        self.driver.find_element(By.NAME, "password").send_keys("admin12323")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_003(self):
        self.driver.find_element(By.NAME, "username").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_004(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_005(self):
        self.driver.find_element(By.NAME, "username").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_006(self):
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_007(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123e")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_008(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("@#$%^")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    def test_009(self):
        self.driver.find_element(By.NAME, "username").send_keys("!@#$%^")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()