from selenium import webdriver
import pytest
from Framework.Pages.login import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    obj=LoginPage(driver)