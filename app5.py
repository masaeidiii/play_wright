from playwright.sync_api import Playwright, sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel='chrome')

    page= browser.new_page()
    page.goto('https://stdn.iau.ir/Student/Pages/acmstd/loginPage.jsp')
    page.locator("#user").fill('404709433')
    page.locator("#pass").fill('m8833')

    captcha= input('print the code:')
    page.locator("input[name='jcaptcha']").fill('captcha')

    page.get_by_role("button", name="ورود به سيستم").click()
    

    page.pause()