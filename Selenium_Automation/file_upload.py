#Script to upload a file using Selenium WebDriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
url = "https://formy-project.herokuapp.com/fileupload"
driver.get(url)
time.sleep(3)

driver.find_element(By.ID, "file-upload-field").send_keys("/Users/sanjeevparajuli/Downloads/Malyasia Airport.png")
time.sleep(3)
driver.quit()
