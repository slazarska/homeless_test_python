import allure
from selene import be, have
from selene.support.shared import browser

from homeless_test_python.model.data.messages import Messages


@allure.step("Проверить, что страница пожертвований открылась в новой вкладке браузера")
def check_help_page_is_opened():
    browser.switch_to_next_tab()
    browser.config.timeout = 15
    browser.element('.m-help-page').should(be.visible)


@allure.step("Выбрать одноразовую форму пожертвования")
def choose_one_time_donation():
    browser.element('[data-period="разово"]').should(be.clickable).click()


@allure.step("Выбрать регулярную форму пожертвования")
def choose_regular_donation():
    browser.element('[data-period="ежемесячно"]').should(be.clickable).click()


@allure.step("Проверить выбранную форму пожертвования")
def check_donation_warning(period='text'):
    if period == Messages.ONE_TIME:
        browser.element('.donation-warning').should(have.text(Messages.ONE_TIME_DONATION_WARNING))
    elif period == Messages.REGULAR:
        browser.element('.donation-warning').should(have.text(Messages.REGULAR_DONATION_WARNING))


@allure.step("Выбрать стандартную сумму пожертвования")
def choose_standard_sum_help(amount=int):
    if amount == 300:
        browser.element('label[for="m-help-form-300"]').should(be.clickable).click()
    elif amount == 700:
        browser.element('label[for="m-help-form-700"]').should(be.clickable).click()
    elif amount == 1000:
        browser.element('label[for="m-help-form-1000"]').should(be.clickable).click()
    elif amount == 3000:
        browser.element('label[for="m-help-form-3000"]').should(be.clickable).click()


@allure.step("Проверить сообщение о стандартной сумме пожертвования")
def check_standard_sum_message(amount=int):
    if amount == 300:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(Messages.THREE_HUNDRED_MESSAGE))
    elif amount == 700:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(Messages.SEVEN_HUNDRED_MESSAGE))
    elif amount == 1000:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(Messages.ONE_THOUSAND_MESSAGE))
    elif amount == 3000:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(Messages.THREE_THOUSAND_MESSAGE))


@allure.step("Ввести корректное имя пользователя в поле формы для отправки пожертвования")
def set_username(test_data='name'):
    browser.element('[name="help-transfer-name"]').type(test_data).press_tab()


@allure.step("Ввести корректный адрес электронной почты в поле формы для отправки пожертвования")
def set_email(test_data='email'):
    browser.element('[name="help-transfer-email"]').type(test_data).press_tab()


@allure.step("Проверить, что кнопка подтверждения отправки пожертвования активна")
def check_submit_button():
    browser.element('button[type="submit"]').should(be.clickable)


@allure.step("Нажать кнопку подтверждения отправки пожертвования")
def click_on_submit_button():
    browser.element('button[type="submit"]').click()


@allure.step("Проверить сообщение об ошибке в форме отправки пожертвования")
def check_error_message():
    browser.element('label[id="help-transfer-email-error"]').should(have.text("Заполните, пожалуйста"))


@allure.step("Проверить отсутствие сообщения об ошибке в форме отправки пожертвования")
def check_error_message_is_missing():
    browser.element('label[id="help-transfer-email-error"]').should(be.absent)
