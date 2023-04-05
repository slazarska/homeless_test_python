import allure
from allure_commons.types import Severity

from homeless_test_python.model import app


@allure.tag("ui", "web")
@allure.label("owner", "slazarska")
@allure.feature("Основная функциональность")
@allure.story("Главная страница")
class TestMainPage:

    @allure.severity(Severity.BLOCKER)
    @allure.description("Тест открывает главную страницу сайта и проверяет, что страница загружена")
    def test_open_main_page(self):
        app.main_page.open_main_page()
        app.main_page.check_main_page_is_opened()

    @allure.severity(Severity.CRITICAL)
    @allure.description("Тест открывает на главной странице ссылку на страницу пожертвований и"
                        " проверяет, что страница пожертвований открылась в новой владке браузера")
    def test_switch_on_help_page(self):
        app.main_page.open_main_page()
        app.main_page.click_help_button()
        app.help_page.check_help_page_is_opened()
