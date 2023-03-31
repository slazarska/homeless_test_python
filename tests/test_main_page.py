import allure
from allure_commons.types import Severity

from homeless_test_python.model.pages import mainpage, helppage


@allure.label("owner", "slazarska")
@allure.feature("Основная функциональность")
@allure.story("Главная страница")
class TestMainPage:

    @allure.severity(Severity.BLOCKER)
    @allure.description("Тест открывает главную страницу сайта и проверяет, что страница загружена")
    def test_open_main_page(self):
        mainpage.open_main_page()
        mainpage.check_main_page_is_opened()

    @allure.severity(Severity.CRITICAL)
    @allure.description("Тест открывает на главной странице ссылку на страницу пожертвований и"
                        " проверяет, что страница пожертвований открылась в новой владке браузера")
    def test_switch_on_help_page(self):
        mainpage.open_main_page()
        mainpage.click_help_button()
        helppage.check_help_page_is_opened()
