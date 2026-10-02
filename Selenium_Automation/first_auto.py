# Import modules
from selenium import webdriver
import time

# initialize driver
driver = webdriver.Chrome()
time.sleep(1)

# maximize window
driver.maximize_window()

# delay execution using time module
time.sleep(2)

url = "https://google.com"

# navigates to url
driver.get(url)
time.sleep(2)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

# print title and current url
print("The page title is: ", driver.title)

# print current url
print("The current url is: ", driver.current_url)

# Quit Driver and browser
driver.quit()