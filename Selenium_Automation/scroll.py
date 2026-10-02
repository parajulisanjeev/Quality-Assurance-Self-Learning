# Script to scroll down the page using Selenium WebDriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
url = "https://formy-project.herokuapp.com/scroll"
driver.get(url)
time.sleep(3)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Sanjeev Parajuli")
driver.find_element(By.ID, "date").send_keys("01/01/2024")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "date").clear()
time.sleep(3)


driver.quit()