import time

from Locators import locators


class Registration:

    def __init__(self, driver):
        self.driver = driver
        self.emailField = locators.emailField
        self.passwordField = locators.passwordField
        self.phoneField = locators.phoneField
        self.signUpButton = locators.signUpButton

    #Function selects Email field and enters email input

    def ClickOnEmailField(self, email):
        self.driver.find_element_by_css_selector(self.emailField).click()
        self.driver.find_element_by_css_selector(self.emailField).send_keys(email)
        time.sleep(2)

    # Function selects Password field and enters password input

    def ClickOnPasswordField(self, password ):
        self.driver.find_element_by_css_selector(self.passwordField).click()
        self.driver.find_element_by_css_selector(self.passwordField).send_keys(password)
        time.sleep(2)

    # Function selects Mobile field and enters mobile input

    def ClickOnMobileField(self, mobile):
       self.driver.find_element_by_css_selector(self.phoneField).click()
       self.driver.find_element_by_css_selector(self.phoneField).send_keys(mobile)
       time.sleep(2)

    #Clicks Submmit button

    def ClickOnSignUpButton(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element_by_css_selector(self.signUpButton).click()
        print(self.driver.title)
        print('Account was created successfully!')



