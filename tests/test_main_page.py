import allure
from allure_commons.types import Severity

from homeless_test_python.model.pages import mainpage


@allure.tag("UI")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "slazarska")
@allure.feature("Main Functionality")
@allure.story("Open Main Page")
@allure.description("Open main page and check the main page is loaded")
def test_open_main_page():
    mainpage.open_main_page()
    mainpage.check_main_page_is_opened()
