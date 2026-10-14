from playwright.sync_api import sync_playwright
from login import Loginpage

def test_login():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False, slow_mo=(3000))
        page=browser.new_page()

        page.goto("https://www.saucedemo.com")
        login=Loginpage(page)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        browser.close()