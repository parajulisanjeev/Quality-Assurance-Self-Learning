from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

login_url = "https://www.saucedemo.com/"
username_locator = (By.ID, "user-name")
password_locator = (By.ID, "password")
login_button_locator = (By.ID, "login-button")

driver = webdriver.Chrome()
driver.maximize_window()

#define test function
def login_test(username, password):
    driver.get(login_url)
    time.sleep(2)  # Wait for the page to load

    driver.find_element(*username_locator).clear()
    driver.find_element(*username_locator).send_keys(username)
    time.sleep(2)  # Wait for the input to be registered

    driver.find_element(*password_locator).clear()
    driver.find_element(*password_locator).send_keys(password)
    time.sleep(2)  # Wait for the input to be registered

    driver.find_element(*login_button_locator).click()
    time.sleep(2)  # Wait for the page to load

with open('users.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row['username']
        password = row['password']
        login_test(username, password)

driver.quit()