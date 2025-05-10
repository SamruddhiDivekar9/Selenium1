from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/Akash%20Divekar/Downloads/demo.html")
sleep(2)

single_select=driver.find_element(By.ID,"standard_cars")

sel=Select(single_select)

sel.select_by_visible_text("Audi")
sleep(2)

sel.select_by_value("jgr")
sleep(2)

sel.select_by_index(7)
sleep(2)


# sel.deselect_by_index(7)
# sleep(2)

"""

when you are trying to perform deselect in sinhgle select dropdown it will throw the exception
----> 

Traceback (most recent call last):
  File "C:\\Akash Divekar\PycharmProjects\com.crm.SeleniumPYM1\Selenium\Select Class\SingleSelectDropdown.py", line 27, in <module>
    sel.deselect_by_index(7)
    ~~~~~~~~~~~~~~~~~~~~~^^^
  File "C:\\Akash Divekar\PycharmProjects\com.crm.SeleniumPYM1\Selenium\.venv\Lib\site-packages\selenium\webdriver\support\select.py", line 183, in deselect_by_index
    raise NotImplementedError("You may only deselect options of a multi-select")
NotImplementedError: You may only deselect options of a multi-select
"""


