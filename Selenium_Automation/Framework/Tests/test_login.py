from Pages.login import LoginPage
import pytest

@pytest.mark.parametrize("username, password",[
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
])

def test_login(driver, username, password):
    obj=LoginPage(driver)
    obj.open_url("https://saucedemo.com")
    obj.enter_username(username)
    obj.enter_password(password)
    obj.click_login_button()
    assert "inventory" in obj.driver.current_url, "Login failed, user not redirected to inventory page"

# def test_invalid_login(driver):
#      obj=LoginPage(driver)
#      obj.open_url("https://saucedemo.com")
#      obj.enter_username("invalid_user")
#      obj.enter_password("invalid_password")
#      obj.click_login_button()
#      assert "inventory" not in obj.driver.current_url, "Login succeeded with invalid credentials, user should not be redirected to inventory page"