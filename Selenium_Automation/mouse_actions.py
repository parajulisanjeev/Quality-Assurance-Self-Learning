from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

# Mouse Actions
actions = ActionChains(driver)
# actions.move_to_element(login_button).click().perform()  # Move to the login button and click it
actions.click_and_hold(login_button).perform()  # Click and hold the login button
time.sleep(2)
actions.release().perform()  # Release the click
time.sleep(2)

driver.quit()