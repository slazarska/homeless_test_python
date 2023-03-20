import pytest

from homeless_test_python import app
import allure
from allure_commons.types import Severity


@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Регулярные пожертвования")
@allure.description("Тест проверяет, что по умолчанию выбраны регулярные пожертвования")
def test_choose_default_state_of_donation(how_to_help):
    app.howtohelp.check_donation_warning(app.Messages.REGULAR_DONATION_WARNING)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Разовые пожертвования")
@allure.description("Тест проверяет возможность выбрать одноразовое пожертвование")
def test_choose_of_one_time_donation(how_to_help):
    app.howtohelp.choose_one_time_donation()
    app.howtohelp.check_donation_warning(app.Messages.ONE_TIME_DONATION_WARNING)
    '''
    add the check of payments methods
    '''


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Регулярные пожертвования")
@allure.description("Тест проверяет возможность выбрать регулярные пожертвования")
def test_choose_regular_donation(how_to_help):
    app.howtohelp.choose_regular_donation()
    app.howtohelp.check_donation_warning(app.Messages.REGULAR_DONATION_WARNING)
    '''
    add the check of payments methods
    '''


@pytest.mark.skip(reason="work in progress")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Регулярные пожертвования")
@allure.description("Тест проверяет выбор стандартной суммы для регулярных пожертвований")
def test_choose_sum_of_regular_donation(how_to_help):
    app.howtohelp.choose_regular_donation()
    app.howtohelp.choose_standard_sum_help(300)
    app.howtohelp.check_standard_sum_message(300)


@pytest.mark.skip(reason="work in progress")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Разовые пожертвования")
@allure.description("Тест проверяет выбор стандартной суммы для одноразового пожертвования")
def test_choose_sum_of_one_time_donation(how_to_help):
    app.howtohelp.choose_one_time_donation()
    app.howtohelp.choose_standard_sum_help(1000)
    app.howtohelp.check_standard_sum_message(1000)


@pytest.mark.skip(reason="work in progress")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Форма для отправки пожертвования")
@allure.description("Тест проверяет заполнение полей формы для отправки пожертвования корректными данными, "
                    "отсутствие ошибок после заполнения формы и возможность нажать кнопку подтверждения")
def test_fill_the_donate_form_with_valid_data(how_to_help):
    app.howtohelp.set_username(app.User.name)
    app.howtohelp.set_email(app.User.email)
    app.howtohelp.check_submit_button()


@pytest.mark.skip(reason="work in progress")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Пожертвования")
@allure.story("Форма для отправки пожертвования")
@allure.description("Тест проверяет, что поле для электронной почты обязательно для заполнения в форме "
                    "отправки пожертвования")
def test_fill_the_donate_form_with_valid_data(how_to_help):
    app.howtohelp.set_username(app.User.name)
    app.howtohelp.check_submit_button()
