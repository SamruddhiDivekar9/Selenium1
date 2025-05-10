from seleniumpagefactory.Pagefactory import PageFactory

class Home(PageFactory):
    def __init__(self,driver):
        self.driver=driver

    locators = {'leave_page': ("XPATH", '//nav[@class="oxd-navbar-nav"]/div[2]//li[3]/a'),
                "user": ("CLASS_NAME", "oxd-userdropdown-tab"),
                "logout": ("LINK_TEXT", 'Logout')
                }

    def click_leave(self):
        self.leave_page.click()

    def click_user(self):
        self.user.click()

    def click_logout(self):
        self.logout.click()
