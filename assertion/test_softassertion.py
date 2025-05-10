from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    print("im in dws page")
    radio_button=driver.find_element(By.ID,"pollanswers-1")
    assert radio_button.is_selected(),"radio button is not selected"
    print("radio button is selected")