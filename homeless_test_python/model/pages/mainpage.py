import allure
from selene.support.shared import browser
from selene import be


@allure.step("Open Main Page")
def open_main_page():
    browser.open('https://homeless.ru/')


@allure.step("Check the main page is opened")
def check_main_page_is_opened():
    browser.element('.logo-main').should(be.visible)