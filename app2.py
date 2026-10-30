import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click()
    page.goto("https://www.varzesh3.com/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="ویدیو", description="ویدیو").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="خلاصه بازی بورنموث 3 - میلان 0 03:").first.click()
    page1.get_by_role("button", name="توقف").click()
    page1.get_by_role("banner").get_by_role("link", name="خلاصه بازی").click()
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="خلاصه بازی بورنموث 3 - میلان").click()
    page2 = page2_info.value
    page2.get_by_role("button", name="توقف").click()

    # ---------------------
   #context.close()
   #rowser.close()
    page.pause()


with sync_playwright() as playwright:
    run(playwright)
