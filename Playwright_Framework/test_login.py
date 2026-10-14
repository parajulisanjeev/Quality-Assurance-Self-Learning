from playwright.sync_api import Page, expect
from login import LoginPage


def test_login(page: Page):

    page.goto("https://www.saucedemo.com")

    login = LoginPage(page)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")