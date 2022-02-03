import time
from selenium import webdriver
from HomePage.HomePage import Home
from RegistrationPage.RegistrationPage import Registration
from LoginPage.LoginPage import Login
import GlobalVariables

driver = webdriver.Chrome("/Applications/chromedriver")
driver.get(GlobalVariables.website)
print(driver.title)
driver.maximize_window()
time.sleep(3)



def HomePage():
    user = Home(driver)
    user.ConfirmCookies()
    user.HeaderButtonLogin()


def JoinZyroPage():
    user = Login(driver)
    user.AccountLink()


def RegisterPage():
    user = Registration(driver)
    user.ClickOnEmailField(GlobalVariables.email)
    user.ClickOnPasswordField(GlobalVariables.password)
    user.ClickOnMobileField(GlobalVariables.mobile)
    user.ClickOnSignUpButton()




HomePage()
JoinZyroPage()
RegisterPage()

