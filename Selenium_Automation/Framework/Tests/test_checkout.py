from Pages.login import LoginPage
from Pages.inventory import InventoryPage
from Pages.checkout import CheckoutPage


def test_checkout(driver):

    # Login
    login = LoginPage(driver)

    login.open_url("https://www.saucedemo.com/")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()

    # Add product to cart
    inventory = InventoryPage(driver)

    inventory.click_add_to_cart()

    # Checkout process
    checkout = CheckoutPage(driver)

    checkout.click_cart()
    checkout.click_checkout()

    # Enter customer information
    checkout.enter_first_name("Sanjeev")
    checkout.enter_last_name("Parajuli")
    checkout.enter_postal_code("44600")

    # Continue checkout
    checkout.click_continue()

    # Finish order
    checkout.click_finish()

    # Verify order completed
    assert "checkout-complete.html" in driver.current_url

    print("Order Successful")