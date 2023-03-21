import allure
from allure_commons.types import Severity

from homeless_test_python.model.pages import mainpage


@allure.severity(Severity.BLOCKER)
@allure.label("owner", "slazarska")
@allure.feature("Основная функциональность")
@allure.story("Главная страница")
@allure.description("Тест открывает главную страницу сайта и проверяет, что страница загружена")
def test_open_main_page():
    mainpage.open_main_page()
    mainpage.check_main_page_is_opened()
