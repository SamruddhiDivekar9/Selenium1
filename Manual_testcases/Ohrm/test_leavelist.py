from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup2")
class TestCase2:
    def test_list(self):
        self.driver.find_element(By.XPATH, '//nav[@class="oxd-navbar-nav"]/div[2]//li[3]/a').click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Leave List").click()
        sleep(2)
        act=ActionChains(self.driver)
        upto = self.driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
        act.double_click(upto).click().perform()
        upto.send_keys("2025-12-05")

        fromd = self.driver.find_element(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
        act.double_click(fromd).click().perform()
        fromd.send_keys("2025-10-05")
        sleep(4)

        self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        act.release()

        self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(
            Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        act.release()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("James Butler")
        sleep(2)

        self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[3]").click()
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        sleep(2)
        act.release()
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

