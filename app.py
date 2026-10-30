from playwright.sync_api import sync_playwright

with sync_playwright() as p :
    browser = p.chromium.launch(headless = False , channel='chrome' ) 

    page = browser.new_page() 
    #page.goto('https://google.com')
    #page.goto('https://varzesh3.com')
    page.goto('https://divar.ir') 
    page.get_by_role("link", name="اهواز").click() 
    page.get_by_role("button", name=" دیوار من").click() 
    page.get_by_role("button", name=" ورود به حساب کاربری").click()
    page.get_by_placeholder("۰۹۱۲ ۳۴۵ ۶۷۸۹").fill('09364281733')
    page.get_by_role("button", name="بعدی").click() 
    page.get_by_role("textbox", name="جستجو در همهٔ آگهی‌ها").fill('ماشین اروند')



    page.pause()