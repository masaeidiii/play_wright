import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://esale.ikco.ir/")
    page.get_by_label("من ربات نیستم").click()
    page.locator("img").nth(3).click()
    page.locator("div:nth-child(10) > .background-layer > .tw-rounded-xl").click()
    page.locator("#submit-btn").click()
    page.get_by_role("textbox", name="کد كاربري").click()
    page.get_by_role("textbox", name="کد كاربري").fill("1750880458")
    page.get_by_role("textbox", name="كلمه عبور").click()
    page.get_by_role("textbox", name="كلمه عبور").press("CapsLock")
    page.get_by_role("textbox", name="كلمه عبور").fill("FA")
    page.get_by_role("textbox", name="كلمه عبور").press("CapsLock")
    page.get_by_role("textbox", name="كلمه عبور").fill("FAr1346!@#$")
    page.locator("#captchaCode").click()
    page.locator("#captchaCode").fill("40")
    page.locator("#captchaCode").click()
    page.locator("#captchaCode").fill("")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
