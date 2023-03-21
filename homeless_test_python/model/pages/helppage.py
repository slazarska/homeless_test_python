import allure
from selene import be, have
from selene.support.shared import browser

ONE_TIME = 'one-time'
REGULAR = 'regular'
THREE_HUNDRED_MESSAGE = '300 рублей'
ONE_TIME_DONATION_WARNING = 'Вы выбрали разовое пожертвование'
REGULAR_DONATION_WARNING = 'Вы выбрали регулярные пожертвования'
THREE_HUNDRED_MESSAGE = '300 рублей'
SEVEN_HUNDRED_MESSAGE = '700 рублей'
ONE_THOUSAND_MESSAGE = '1 000 рублей'
THREE_THOUSAND_MESSAGE = '3 000 рублей'


@allure.step("Выбрать одноразовую форму пожертвования")
def choose_one_time_donation():
    browser.element('[data-period="разово"]').should(be.clickable).click()


@allure.step("Выбрать регулярную форму пожертвования")
def choose_regular_donation():
    browser.element('[data-period="ежемесячно"]').should(be.clickable).click()


@allure.step("Проверить выбранную форму пожертвования")
def check_donation_warning(period='text'):
    if period == ONE_TIME:
        browser.element('.donation-warning').should(have.text(ONE_TIME_DONATION_WARNING))
    elif period == REGULAR:
        browser.element('.donation-warning').should(have.text(REGULAR_DONATION_WARNING))


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
            .should(have.text(THREE_HUNDRED_MESSAGE))
    elif amount == 700:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(SEVEN_HUNDRED_MESSAGE))
    elif amount == 1000:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(ONE_THOUSAND_MESSAGE))
    elif amount == 3000:
        browser.element('p[class="form-donate__sum--desc active"]') \
            .should(have.text(THREE_THOUSAND_MESSAGE))


@allure.step("Ввести корректное имя в поле формы для отправки пожертвования")
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
