import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://divar.ir/")
    page.get_by_role("link", name="اهواز").click()
    page.get_by_role("button", name=" دیوار من").click()
    page.get_by_role("button", name=" ورود به حساب کاربری").click()
    page.get_by_placeholder("۰۹۱۲ ۳۴۵ ۶۷۸۹").click()
    page.get_by_placeholder("۰۹۱۲ ۳۴۵ ۶۷۸۹").fill("۰۹۳۶ ۴۲۸ ۱۷۳3")
    page.get_by_role("button", name="بعدی").click()
    page.get_by_role("textbox", name="جستجو در همهٔ آگهی‌ها").click()
    page.get_by_role("textbox", name="جستجو در همهٔ آگهی‌ها").fill("ماشین")
    page.get_by_text("جستجوی «ماشین»").click()

    # ---------------------
    #context.close()
    #browser.close()
    page.pause()

with sync_playwright() as playwright:
    run(playwright)
