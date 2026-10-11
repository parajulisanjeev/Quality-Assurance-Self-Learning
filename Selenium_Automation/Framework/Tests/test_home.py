import time
from Pages.home import HomePage
from Pages.login import LoginPage


def test_home(driver):
    login = LoginPage(driver)

    login.open_url("https://saucedemo.com")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()
    time.sleep(2)
    obj=HomePage(driver)
    obj.click_addtocart()
    time.sleep(2)

