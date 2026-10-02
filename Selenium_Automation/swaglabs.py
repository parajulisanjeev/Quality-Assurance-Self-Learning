from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://saucedemo.com"
driver.get(url)
# driver.implicitly_wait(10)

driver.find_element("id", "user-name").send_keys("standard_user")
driver.find_element("id", "password").send_keys("secret_sauce")
time.sleep(3)
# driver.find_element("id", "login-button").click()

wait = WebDriverWait(driver, 10)
try:
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    time.sleep(3)

except:
    print("Login button not found or not clickable")

finally:
    print("Login attempt completed")

# assertion or login verification
# if driver.current_url == "https://www.saucedemo.com/inventory.html":
#     print("Login successful")
# else:
#     print("Login failed")

# if "inventory" in driver.current_url:
#     print("Login successful")
# else:
#     print("Login failed")

# assert "inventory" in driver.current_url, "Login Failed"

alert=driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(3)

driver.close()
driver.quit()