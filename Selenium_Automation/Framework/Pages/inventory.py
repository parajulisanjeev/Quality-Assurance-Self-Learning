from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

        self.sort_dropdown = (By.XPATH, "//select[@aria-label='Sort products']")
        self.add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_from_cart = (By.ID, "remove-sauce-labs-backpack")

    def sort_products(self, option):
        dropdown = self.driver.find_element(*self.sort_dropdown)
        select = Select(dropdown)
        select.select_by_visible_text(option)
        print("Sorted by:", option)
        time.sleep(2)

    def get_selected_sort_option(self):
        dropdown = self.driver.find_element(*self.sort_dropdown)
        select = Select(dropdown)
        return select.first_selected_option.text

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()
        print("Product added to cart")
        time.sleep(2)

    def click_remove_from_cart(self):
        self.driver.find_element(*self.remove_from_cart).click()
        print("Product removed from cart")
        time.sleep(2)

    def remove_button_displayed(self):
        return self.driver.find_element(*self.remove_from_cart).is_displayed()

    def add_to_cart_button_displayed(self):
        return self.driver.find_element(*self.add_to_cart).is_displayed()