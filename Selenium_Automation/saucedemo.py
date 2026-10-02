from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)

url = "https://saucedemo.com"
driver.get(url)

time.sleep(1)

driver.quit()
