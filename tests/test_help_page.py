import allure
import pytest
from allure_commons.types import Severity

from homeless_test_python.model.data.messages import Messages
from homeless_test_python.model.data.user import test_user
from homeless_test_python.model.pages import helppage

test_data = [300, 700, 1000, 3000]


@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
class TestHelpPage:

    @allure.severity(Severity.NORMAL)
    @allure.story("Регулярные пожертвования")
    @allure.description("Тест проверяет, что по умолчанию выбраны регулярные пожертвования")
    def test_choose_default_state_of_donation(self, how_to_help):
        helppage.check_donation_warning(Messages.REGULAR_DONATION_WARNING)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Разовые пожертвования")
    @allure.description("Тест проверяет возможность выбрать одноразовое пожертвование")
    def test_choose_of_one_time_donation(self, how_to_help):
        helppage.choose_one_time_donation()
        helppage.check_donation_warning(Messages.ONE_TIME_DONATION_WARNING)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Регулярные пожертвования")
    @allure.description("Тест проверяет возможность выбрать регулярные пожертвования")
    def test_choose_regular_donation(self, how_to_help):
        helppage.choose_regular_donation()
        helppage.check_donation_warning(Messages.REGULAR_DONATION_WARNING)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Регулярные пожертвования")
    @allure.description("Тест проверяет выбор стандартной суммы для регулярных пожертвований")
    @pytest.mark.parametrize("sum_donation", test_data)
    def test_choose_sum_of_regular_donation(self, how_to_help, sum_donation):
        sum_donation = test_data
        helppage.choose_regular_donation()
        helppage.choose_standard_sum_help(sum_donation)
        helppage.check_standard_sum_message(sum_donation)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Разовые пожертвования")
    @allure.description("Тест проверяет выбор стандартной суммы для одноразового пожертвования")
    @pytest.mark.parametrize("sum_donation", test_data)
    def test_choose_sum_of_one_time_donation(self, how_to_help, sum_donation):
        sum_donation = test_data
        helppage.choose_one_time_donation()
        helppage.choose_standard_sum_help(sum_donation)
        helppage.check_standard_sum_message(sum_donation)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Форма для отправки пожертвования")
    @allure.description("Тест проверяет заполнение полей формы для отправки пожертвования корректными данными, "
                        "отсутствие ошибок после заполнения формы и возможность нажать кнопку подтверждения")
    def test_fill_the_donate_form_with_valid_data(self, how_to_help):
        helppage.set_username(test_user.name)
        helppage.set_email(test_user.email)
        helppage.check_error_message_is_missing()
        helppage.check_submit_button()

    @allure.severity(Severity.NORMAL)
    @allure.story("Форма для отправки пожертвования")
    @allure.description("Тест проверяет, что поле для электронной почты обязательно для заполнения в форме "
                        "отправки пожертвования")
    def test_email_field_in_donate_form_is_obligatorily(self, how_to_help):
        helppage.set_username(test_user.name)
        helppage.click_on_submit_button()
        helppage.check_error_message()

    @allure.severity(Severity.NORMAL)
    @allure.story("Форма для отправки пожертвования")
    @allure.description("Тест проверяет, что поле для имени необязательно для заполнения в форме "
                        "отправки пожертвования")
    def test_name_field_in_donate_form_is_not_obligatorily(self, how_to_help):
        helppage.set_email(test_user.email)
        helppage.check_error_message_is_missing()
        helppage.check_submit_button()
