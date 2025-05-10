from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup2")
class TestCase1:
    def test_assign(self):
        self.driver.find_element(By.XPATH, '//nav[@class="oxd-navbar-nav"]/div[2]//li[3]/a').click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Assign Leave").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("James Butler")
        sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
        act=ActionChains(self.driver)
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(
            Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        act.key_up(Keys.ENTER)
        upto = self.driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
        upto.click()
        # upto.clear()
        upto.send_keys("2025-12-05")
        self.driver.find_element(By.XPATH, "//input[@placeholder='yyyy-dd-mm']").send_keys("2025-10-05")
        sleep(4)

        self.driver.find_element(By.TAG_NAME, "textarea").send_keys("Due to some personal reasons I need a leave")
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]").click()
        sleep(1)
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        act.release()
        sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-wrapper'])[3]/div/div").click()
        sleep(1)
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
