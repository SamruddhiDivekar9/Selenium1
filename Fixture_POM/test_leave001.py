from time import sleep
# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Fixture_POM.HomePage import Home
from Fixture_POM.leave import Leave


from PageObjectModel.tc_01 import driver


def test_leave(setup):
    act=ActionChains(driver)
    home = Home(driver)
    leave = Leave(driver)
    home.click_leave()
    leave.assign_leave()
    sleep(2)
    leave.search("Bruce Banner 0077262")
    sleep(2)
    leave.drop_1()
    sleep(1)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    sleep(1)
    leave.upto_date("2025-06-05")
    sleep(1)
    leave.from_date("2025-04-05")
    sleep(1)
    leave.reason_d("some reason")
    sleep(1)
    leave.reason_1()
    sleep(1)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    sleep(2)
    act.release()
    sleep(2)
    leave.reason_2()
    sleep(1)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    sleep(1)
    leave.sub2()
    sleep(1)
