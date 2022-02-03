import time

from Locators import locators


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.createAccountLink = locators.registerLink

    #Clicks on the Create account link in the /prisijunk endpoint

    def AccountLink(self):
        self.driver.find_element_by_css_selector(self.createAccountLink).click()
        time.sleep(3)
