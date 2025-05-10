"""
Write a script for guru 99 browser

Open the vr
Max the br
Open the website
Verify the website
Performvright click action on right click me element
Click the elements present in it
Retrieve the text of the popups
Handle the popup-ok
For all
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opt = webdriver.ChromeOptions()

opt.add_experimental_option('detach', True)

dr = webdriver.Chrome(options=opt)
dr.maximize_window()
act = ActionChains(dr)
dr.get('https://demo.guru99.com/test/simple_context_menu.html')

expected_url = 'https://demo.guru99.com/test/simple_context_menu.html'

actual = dr.current_url
if actual == expected_url:
    right = dr.find_element(By.XPATH, '//span[text() = "right click me"]')
    act.context_click(right).perform()

    box = dr.find_elements(By.XPATH, '//ul[@class="context-menu-list context-menu-root"]/li')
    for i in box:
        if i.text.strip() == "":
            continue
        i.click()
        sleep(1)
        alt = dr.switch_to.alert
        print(alt.text)
        alt.accept()
        sleep(1)
        act.context_click(right).perform()
        sleep(1)

sleep(1)
dr.quit()