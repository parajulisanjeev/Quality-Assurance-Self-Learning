from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)

url = "https://saucedemo.com"
driver.get(url)

time.sleep(1)
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

#Actions
username.send_keys("standard_user")
time.sleep(2)
# username.clear()
password.send_keys("secret_sauce")
time.sleep(2)

login_button.click()
time.sleep(2)

#Handling Dropdowns
from selenium.webdriver.support.ui import Select
sort_options = driver.find_element(By.XPATH, "//select[@aria-label='Sort products']") #Using Absolute Xpath to locate the sort options dropdown
select = Select(sort_options)
select.select_by_visible_text("Price (low to high)") #Selecting the option with value "lohi" from the dropdown
time.sleep(2)

# select.deselect_by_value("lohi") #Deselecting the option with value "lohi" from the dropdown if only multiple selections are allowed

# selected=select.first_selected_option
# print("Selected option is: ", selected.text)
# assert selected.text == "Price (low to high)", "Selected option is not as expected"

driver.quit()
