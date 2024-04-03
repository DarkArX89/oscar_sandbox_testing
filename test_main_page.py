from selenium.webdriver.common.by import By

from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
