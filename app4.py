from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless= False, channel= 'chrome')

    page = browser.new_page()
    page.goto('https://adliran.ir')
    page.locator("div").filter(has_text="ابلاغ الکترونیک قضایی").nth(5).click()
    page.get_by_role("link", name="سامانه پشتیبان 1").click()
    page.get_by_label('شناسه افراد').fill('1743158361')
    page.get_by_label('رمز عبور').fill('1469353197')


    page.get_by_role("button", name="مرحله بعد").click()


    page.pause()