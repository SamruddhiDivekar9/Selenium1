from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestCase1:
    def test_admin(self):
        self.driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("admin")
        sleep(2)
        admin=self.driver.find_element(By.XPATH,"//span[text()='Admin']")
        sleep(2)
        assert admin.is_displayed(),"Admin is not present"
        print("admin is present")
    def test_pim(self):
        sleep(2)
        pim=self.driver.find_element(By.XPATH,"//span[text()='PIM']")
        assert pim.is_displayed(),"pim is not displayed"
        print("pim is present")
