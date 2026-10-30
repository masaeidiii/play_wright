import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.technolife.com/")
    page.locator("#menu_categories_button").get_by_role("img").click()
    page.get_by_role("link", name="گوشی آیفون").first.click()

    # ---------------------
    #context.close()
    #browser.close()
    page.pause()


with sync_playwright() as playwright:
    run(playwright)
