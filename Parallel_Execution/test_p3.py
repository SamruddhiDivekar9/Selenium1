from selenium import webdriver

def test_launch1():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    print("im in dws page")
    driver.close()
def test_m1():
    print("im m1")
def test_m2():
    print("im m2")
def test_m3():
    print("im m3")