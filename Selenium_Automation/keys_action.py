from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

# Keyboard Actions
actions = ActionChains(driver)
password.send_keys(Keys.TAB)    # Press Tab to move to the login button
time.sleep(2)
actions.send_keys(Keys.ENTER).perform()  # Press Enter
time.sleep(3)

driver.quit()