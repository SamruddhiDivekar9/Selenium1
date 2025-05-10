
# send_keys("Bruce Banner 0077262")
# sleep(2)
# dr.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
#
# act.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
# sleep(2)
# act.key_up(Keys.ENTER)
# upto=dr.find_element(By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[2]")
# upto.click()
# # upto.clear()
# upto.send_keys("2025-07-05")
# dr.find_element(By.XPATH,"//input[@placeholder='yyyy-dd-mm']").send_keys("2025-06-05")
# sleep(4)
#
# dr.find_element(By.TAG_NAME,"textarea").send_keys("Due to some personal reasons I need a leave")
# sleep(2)
# dr.find_element(By.XPATH,"//button[@type='submit']").click()
#
# dr.find_element(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[2]").click()
# sleep(1)
# act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
# sleep(2)
# act.release()
# sleep(2)
# dr.find_element(By.XPATH,"(//div[@class='oxd-select-wrapper'])[3]/div/div").click()
# sleep(1)
# act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
# sleep(2)
# dr.find_element(By.XPATH,"//button[@type='submit']").click()

from seleniumpagefactory.Pagefactory import PageFactory


class Leave(PageFactory):

    def _init_(self, driver):

        self.driver = driver

    locators = {"assign": ("LINK_TEXT", "Assign Leave"),
                "search_emp": ('XPATH',"//input[@placeholder='Type for hints...']"),
                "drop1": ('XPATH', '//div[@class="oxd-select-text-input"]'),
                "upto": ('XPATH', '(//input[@placeholder="yyyy-dd-mm"])[2]'),
                "from_d": ('XPATH', '(//input[@placeholder="yyyy-dd-mm"])[1]'),
                "reason": ('TAG', 'textarea"]'),
                "submit": ('XPATH', "//button[@type='submit']"),
                "rea1": ('XPATH',"(//div[@class='oxd-select-text oxd-select-text--active'])[2]"),
                "rea2": ('XPATH',"(//div[@class='oxd-select-wrapper'])[3]/div/div"),
                "submit2": ('XPATH', "//button[@type='submit']")
                }

    def assign_leave(self):
        self.assign.click()

    def search(self, data):
        self.search_emp.send_keys(data)

    def drop_1(self):
        self.drop1.click()

    def upto_date(self,data):
        self.upto.send_keys(data)

    def from_date(self, data):
        self.from_d.send_keys(data)

    def reason_d(self, data):
        self.reason.send_keys(data)

    def sub1(self):
        self.submit.click()

    def reason_1(self):
        self.rea1.click()

    def reason_2(self):
        self.rea2.click()

    def sub2(self):
        self.submit2.click()