from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    url=("https://www.saucedemo.com/")
    page.goto(url)
    username = page.locator("#user-name") # Using ID selector
    password = page.locator("#password")
    # login_button = page.locator("#login-button")

    # username=page.get_by_placeholder("Username") - Using placeholder selector
    # password=page.get_by_placeholder("Password")
    # login_button=page.get_by_role("button", name="Login")

    username.fill("standard_user")
    password.fill("secret_sauce")
    password.press("Enter") # Pressing Enter key to submit the form instead of clicking the login button
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("Login successful, navigated to inventory page.")
    page.screenshot(path="/Users/sanjeevparajuli/Desktop/Automation QA/Playwright/screenshot_inventory.png")
    browser.close()