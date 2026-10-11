from selenium.webdriver.common.by import By
import time


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.cart_button = (By.XPATH, "//a[starts-with(@aria-label,'Cart')]")
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def click_cart(self):
        self.driver.find_element(*self.cart_button).click()
        print("Cart opened")
        time.sleep(2)

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        print("Checkout clicked")
        time.sleep(2)

    def enter_first_name(self, firstname):
        self.driver.find_element(*self.first_name).send_keys(firstname)
        time.sleep(2)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.last_name).send_keys(lastname)
        time.sleep(2)

    def enter_postal_code(self, zipcode):
        self.driver.find_element(*self.postal_code).send_keys(zipcode)
        time.sleep(2)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        print("Continue clicked")
        time.sleep(2)

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
        print("Finish clicked")
        time.sleep(2)