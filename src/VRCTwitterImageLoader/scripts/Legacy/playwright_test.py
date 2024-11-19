from playwright.sync_api import sync_playwright


def take_screenshot(url, filename="screenshot.png"):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=30)
        page.screenshot(path=filename)
        browser.close()


# 使用例
if __name__ == "__main__":
    take_screenshot("https://www.google.com", "google_screenshot.png")
