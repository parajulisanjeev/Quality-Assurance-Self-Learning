from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)

url = "https://saucedemo.com"
driver.get(url)

time.sleep(1)
# username = driver.find_element(By.ID, "user-name")
username = driver.find_element(By.XPATH, '//*[@id="user-name"]') #Using Xpath to locate the username field
# password = driver.find_element(By.ID, "password")
password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[2]/input') #Using Absolute Xpath to locate the password field
login_button = driver.find_element(By.ID, "login-button")

#Actions
username.send_keys("standard_user")
time.sleep(2)
username.clear()
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
if login_button.is_enabled():
    print("Login button is enabled")
else:
    print("Login button is disabled")

login_button.click()
time.sleep(3)

driver.quit()
