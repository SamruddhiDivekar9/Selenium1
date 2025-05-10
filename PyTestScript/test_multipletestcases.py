
from selenium import webdriver
# from time import sleep


def test_mi():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("India ka Raja Rohit sharma")
    driver.close()
def test_rcb():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")
    print("yi sala cup namde")
    driver.close()
def test_csk():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")
    print("fixer super king")
    driver.close()