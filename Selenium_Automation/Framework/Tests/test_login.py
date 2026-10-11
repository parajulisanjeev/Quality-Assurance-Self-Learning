from Pages.login import LoginPage

def test_login(driver):
    obj=LoginPage(driver)
    obj.open_url("https://saucedemo.com")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login_button()