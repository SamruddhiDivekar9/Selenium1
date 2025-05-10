from selenium import webdriver
#
# initial steps to avoid closing the browser
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

#open the browser
webdriver.Chrome(options=options)


# EDGE

# options=webdriver.EdgeOptions()
# options.add_experimental_option("detach",True)
# webdriver.Edge(options=options)

# FIREFOX

# options=webdriver.FirefoxOptions()
# options.set_preference("detach",True)
# webdriver.Firefox(options=options)


# ie_options = webdriver.IeOptions()
# ie_options.ignore_protected_mode_settings = True  # Required for IE
#
# driver = webdriver.Ie(options=ie_options)  # Opens Internet Explorer
# driver.get("https://www.google.com")


