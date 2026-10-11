from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver=driver
        self.addtocart=(By.ID, "add-to-cart-sauce-labs-backpack")

    def click_addtocart(self):
        self.driver.find_element(*self.addtocart).click()
        print("Clicked on Add to Cart button")
        time.sleep(2)
