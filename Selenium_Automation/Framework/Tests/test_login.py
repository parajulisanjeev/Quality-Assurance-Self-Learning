from Pages.login import LoginPage

def test_valid_login(driver):
    obj=LoginPage(driver)
    obj.open_url("https://saucedemo.com")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login_button()
    assert "inventory" in obj.driver.current_url, "Login failed, user not redirected to inventory page"

def test_invalid_login(driver):
    obj=LoginPage(driver)
    obj.open_url("https://saucedemo.com")
    obj.enter_username("invalid_user")
    obj.enter_password("invalid_password")
    obj.click_login_button()
    assert "inventory" not in obj.driver.current_url, "Login succeeded with invalid credentials, user should not be redirected to inventory page"