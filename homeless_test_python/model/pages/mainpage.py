import allure
from selene.support.shared import browser
from selene import be


class MainPage:

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        browser.open('https://homeless.ru/')
        return self

    @allure.step("Проверить, что главная страница загрузилась")
    def check_main_page_is_opened(self):
        browser.element('.logo-main').should(be.visible)
        return self

    @allure.step("Нажать кнопку перехода на страницу пожертвований")
    def click_help_button(self):
        browser.element('li.header-banner__item a[href="/how_to_help/"]').click()
        return self
