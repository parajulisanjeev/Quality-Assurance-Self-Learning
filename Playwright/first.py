from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    url=("https://www.saucedemo.com/")
    page.goto(url)
    print(page.title())
    print(page.url)
    # page.screenshot(path="/Users/sanjeevparajuli/Desktop/Automation QA/Playwright/screenshot.png")
    
    browser1 = p.webkit.launch(headless=False, slow_mo=3000)
    page1 = browser1.new_page()
    url=("https://rankwithsanjeev.com/")
    page1.goto(url)
    print(page1.title())
    print(page1.url)

    browser.close()