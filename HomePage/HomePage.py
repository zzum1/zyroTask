import time
from Locators import locators



class Home:

    def __init__(self, driver):
        self.driver = driver
        self.cookieButton = locators.cookiesButton
        self.createAccountButton = locators.createAccountButton
        self.connectLink = locators.connectLink

    #Enable Cookies

    def ConfirmCookies(self):
        self.driver.find_element_by_css_selector(self.cookieButton).click()
        time.sleep(3)

    #Clicks on the connect(Prisijunk!) button in the header.

    def HeaderButtonLogin(self):
        self.driver.find_element_by_css_selector(self.connectLink).click()
        time.sleep(3)


