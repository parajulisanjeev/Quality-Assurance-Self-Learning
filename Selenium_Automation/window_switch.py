from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
url = "https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(3)
switch_window_button = driver.find_element(By.ID, "new-tab-button")
switch_window_button.click()
time.sleep(3)

# Print the current window handle
windows = driver.window_handles
print("Window handles:", windows)
print("Current window handle:", driver.current_window_handle)

# Switch to the new window
driver.switch_to.window(windows[1])
time.sleep(3)
print("Current window handle:", driver.current_window_handle)

assert "https://formy-project.herokuapp.com/" in driver.current_url, "Switch window failed"


driver.quit()