from selenium import webdriver
import pytest
from Pages.home import HomePage
from Pages.login import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_home(driver):
    login = LoginPage(driver)

    login.open_url("https://saucedemo.com")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()
    obj=HomePage(driver)
    obj.click_addtocart()
