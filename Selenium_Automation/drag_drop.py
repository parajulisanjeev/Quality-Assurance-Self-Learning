from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)

url = "https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
time.sleep(2)

# Drag and Drop
source_element = driver.find_element(By.XPATH, "//div[@id='image']//img")
target_element = driver.find_element(By.XPATH, "//div[@id='box']")
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()
time.sleep(2)


driver.quit()