from Pages.login import LoginPage
from Pages.inventory import InventoryPage


def test_inventory(driver):

    # Login
    login = LoginPage(driver)

    login.open_url("https://www.saucedemo.com/")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()

    # Create Inventory Page object
    inventory = InventoryPage(driver)

    # Sort Name A to Z
    inventory.sort_products("Name (A to Z)")
    assert inventory.get_selected_sort_option() == "Name (A to Z)"

    # Sort Name Z to A
    inventory.sort_products("Name (Z to A)")
    assert inventory.get_selected_sort_option() == "Name (Z to A)"

    # Sort Price Low to High
    inventory.sort_products("Price (low to high)")
    assert inventory.get_selected_sort_option() == "Price (low to high)"

    # Sort Price High to Low
    inventory.sort_products("Price (high to low)")
    assert inventory.get_selected_sort_option() == "Price (high to low)"

    # Add product to cart
    inventory.click_add_to_cart()

    assert inventory.remove_button_displayed()

    # Remove product from cart
    inventory.click_remove_from_cart()

    assert inventory.add_to_cart_button_displayed()