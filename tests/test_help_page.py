import allure
import pytest
from allure_commons.types import Severity

from homeless_test_python.model import app


test_data = [300, 700, 1000, 3000]


@allure.tag("ui", "web")
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
class TestHelpPage:

    @allure.severity(Severity.NORMAL)
    @allure.story("Регулярные пожертвования")
    @allure.description("Тест проверяет, что по умолчанию выбраны регулярные пожертвования")
    def test_choose_default_state_of_donation(self, how_to_help):
        app.help_page.open_help_page()
        app.help_page.check_donation_warning(app.message.REGULAR_DONATION_WARNING)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Разовые пожертвования")
    @allure.description("Тест проверяет возможность выбрать одноразовое пожертвование")
    def test_choose_of_one_time_donation(self, how_to_help):
        app.help_page.open_help_page()
        app.help_page.choose_one_time_donation()
        app.help_page.check_donation_warning(app.message.ONE_TIME_DONATION_WARNING)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Регулярные пожертвования")
    @allure.description("Тест проверяет возможность выбрать регулярные пожертвования")
    def test_choose_regular_donation(self, how_to_help):
        app.help_page.open_help_page()
        app.help_page.choose_regular_donation()
        app.help_page.check_donation_warning(app.message.REGULAR_DONATION_WARNING)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Регулярные пожертвования")
    @allure.description("Тест проверяет выбор стандартной суммы для регулярных пожертвований")
    @pytest.mark.parametrize("sum_donation", test_data)
    def test_choose_sum_of_regular_donation(self, how_to_help, sum_donation):
        app.help_page.open_help_page()
        app.help_page.choose_regular_donation()
        app.help_page.choose_standard_sum_help(sum_donation)
        app.help_page.check_standard_sum_message(sum_donation)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Разовые пожертвования")
    @allure.description("Тест проверяет выбор стандартной суммы для одноразового пожертвования")
    @pytest.mark.parametrize("sum_donation", test_data)
    def test_choose_sum_of_one_time_donation(self, how_to_help, sum_donation):
        app.help_page.open_help_page()
        app.help_page.choose_one_time_donation()
        app.help_page.choose_standard_sum_help(sum_donation)
        app.help_page.check_standard_sum_message(sum_donation)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Форма для отправки пожертвования")
    @allure.description("Тест проверяет заполнение полей формы для отправки пожертвования корректными данными, "
                        "отсутствие ошибок после заполнения формы и возможность нажать кнопку подтверждения")
    def test_fill_the_donate_form_with_valid_data(self, how_to_help):
        app.help_page.open_help_page()
        app.help_page.set_username(app.test_user.name)
        app.help_page.set_email(app.test_user.email)
        app.help_page.check_error_message_is_missing()
        app.help_page.check_submit_button()

    @allure.severity(Severity.NORMAL)
    @allure.story("Форма для отправки пожертвования")
    @allure.description("Тест проверяет, что поле для электронной почты обязательно для заполнения в форме "
                        "отправки пожертвования")
    def test_email_field_in_donate_form_is_obligatorily(self, how_to_help):
        app.help_page.open_help_page()
        app.help_page.set_username(app.test_user.name)
        app.help_page.click_on_submit_button()
        app.help_page.check_error_message()

    @allure.severity(Severity.NORMAL)
    @allure.story("Форма для отправки пожертвования")
    @allure.description("Тест проверяет, что поле для имени необязательно для заполнения в форме "
                        "отправки пожертвования")
    def test_name_field_in_donate_form_is_not_obligatorily(self, how_to_help):
        app.help_page.open_help_page()
        app.help_page.set_email(app.test_user.email)
        app.help_page.check_error_message_is_missing()
        app.help_page.check_submit_button()
