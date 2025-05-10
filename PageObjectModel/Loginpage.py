from seleniumpagefactory.Pagefactory import PageFactory

class Login(PageFactory):
    def __init__(self,driver):
        self.driver=driver

    locators = {'username': ("NAME", "username"),
                "password": ("NAME", "password"),
                "login_button": ("TAG", 'button')
                }

    def send_username(self, data):
        self.username.send_keys(data)

    def send_password(self, pas):
        self.password.send_keys(pas)

    def click_login(self):
        self.login_button.click()
