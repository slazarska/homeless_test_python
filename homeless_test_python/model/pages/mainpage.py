import allure
from selene.support.shared import browser
from selene import be


@allure.step("Открыть главную страницу")
def open_main_page():
    browser.open('https://homeless.ru/')


@allure.step("Проверить, что главная страница загрузилась")
def check_main_page_is_opened():
    browser.element('.logo-main').should(be.visible)


@allure.step("Нажать кнопку перехода на страницу пожертвований")
def click_help_button():
    browser.element('li.header-banner__item a[href="/how_to_help/"]').click()
