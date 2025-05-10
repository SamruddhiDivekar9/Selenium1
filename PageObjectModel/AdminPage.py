from seleniumpagefactory.Pagefactory import PageFactory


class Admin(PageFactory):

    def _init_(self, driver):

        self.driver = driver

    locators = {"add": ("XPATH", '//button[text()=" Add "]'),
                "user_role": ('XPATH', '//div[text()="-- Select --"]'),
                "status": ('XPATH', '(//div[text()="-- Select --"])[1]'),
                "emp_name": ('XPATH', '//input[@placeholder="Type for hints..."]'),
                "username": ('XPATH', '(//input[@class="oxd-input oxd-input--active"])[2]'),
                "pasw": ('XPATH', '//input[@type="password"]'),
                "conf_pas": ('XPATH', '(//input[@type="password"])[2]'),
                "save": ('XPATH', '//button[text()=" Save "]')}

    def adda(self):
        self.add.click()

    def user(self):
        self.user_role.click()

    def stat(self):
        self.status.click()

    def emp(self):
        self.emp_name.click()

    def send_emp(self, data):
        self.emp_name.send_keys(data)

    def send_username(self, data):
        self.username.send_keys(data)

    def send_password(self, data):
        self.pasw.send_keys(data)

    def send_conf_password(self, data):
        self.conf_pas.send_keys(data)

    def click_save(self):
        self.save.click()