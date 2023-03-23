import allure
from allure_commons.types import Severity

from homeless_test_python.model.pages import helppage
from homeless_test_python.model.data.user import test_user


@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Регулярные пожертвования")
@allure.description("Тест проверяет, что по умолчанию выбраны регулярные пожертвования")
def test_choose_default_state_of_donation(how_to_help):
    helppage.check_donation_warning(helppage.REGULAR_DONATION_WARNING)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Разовые пожертвования")
@allure.description("Тест проверяет возможность выбрать одноразовое пожертвование")
def test_choose_of_one_time_donation(how_to_help):
    helppage.choose_one_time_donation()
    helppage.check_donation_warning(helppage.ONE_TIME_DONATION_WARNING)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Регулярные пожертвования")
@allure.description("Тест проверяет возможность выбрать регулярные пожертвования")
def test_choose_regular_donation(how_to_help):
    helppage.choose_regular_donation()
    helppage.check_donation_warning(helppage.REGULAR_DONATION_WARNING)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Регулярные пожертвования")
@allure.description("Тест проверяет выбор стандартной суммы для регулярных пожертвований")
def test_choose_sum_of_regular_donation(how_to_help):
    helppage.choose_regular_donation()
    helppage.choose_standard_sum_help(300)
    helppage.check_standard_sum_message(300)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Разовые пожертвования")
@allure.description("Тест проверяет выбор стандартной суммы для одноразового пожертвования")
def test_choose_sum_of_one_time_donation(how_to_help):
    helppage.choose_one_time_donation()
    helppage.choose_standard_sum_help(3000)
    helppage.check_standard_sum_message(3000)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Форма для отправки пожертвования")
@allure.description("Тест проверяет заполнение полей формы для отправки пожертвования корректными данными, "
                    "отсутствие ошибок после заполнения формы и возможность нажать кнопку подтверждения")
def test_fill_the_donate_form_with_valid_data(how_to_help):
    helppage.set_username(test_user.name)
    helppage.set_email(test_user.email)
    helppage.check_error_message_is_missing()
    helppage.check_submit_button()


@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Форма для отправки пожертвования")
@allure.description("Тест проверяет, что поле для электронной почты обязательно для заполнения в форме "
                    "отправки пожертвования")
def test_fill_the_donate_form(how_to_help):
    helppage.set_username(test_user.name)
    helppage.click_on_submit_button()
    helppage.check_error_message()


@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Форма для отправки пожертвования")
@allure.description("Тест проверяет, что поле для имени необязательно для заполнения в форме "
                    "отправки пожертвования")
def test_fill_the_donate_form(how_to_help):
    helppage.set_email(test_user.email)
    helppage.check_error_message_is_missing()
    helppage.check_submit_button()
