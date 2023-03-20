import allure
from selene.support.shared import browser
from selene import be, have


#browser().driver().switch_to.window()

ONE_TIME_DONATION_WARNING = 'Вы выбрали разовое пожертвование'
REGULAR_DONATION_WARNING = 'Вы выбрали регулярные пожертвования'
ONE_TIME = 'one-time'
REGULAR = 'regular'
THREE_HUNDRED_MESSAGE = '300 рублей'
SEVEN_HUNDRED_MESSAGE = '700 рублей'
ONE_THOUSAND_MESSAGE = '1000 рублей'
THREE_THOUSAND_MESSAGE = '3000 рублей'


@allure.step("Choose one-time period help")
def choose_one_time_donation():
    browser.element('[data-period="разово"]').should(be.clickable).click()


@allure.step("Choose a regular period help")
def choose_regular_donation():
    browser.open('https://homeless.ru/how_to_help/')
    browser.element('[data-period="ежемесячно"]').should(be.clickable).click()


@allure.step("Check choosed help period")
def check_donation_warning(period):
    if period == ONE_TIME:
        browser.element('.donation-warning').should(have.text(ONE_TIME_DONATION_WARNING))
    elif period == REGULAR:
        browser.element('.donation-warning').should(have.text(REGULAR_DONATION_WARNING))


@allure.step("Choose the standard amount for the donation")
def choose_standard_sum_help(int):
    if int == 300:
        browser.element('[label="m-help-form-300"]').should(be.clickable).click()
    elif int == 700:
        browser.element('[label="m-help-form-700"]').should(be.clickable).click()
    elif int == 1000:
        browser.element('[label="m-help-form-1000"]').should(be.clickable).click()
    elif int == 3000:
        browser.element('[label="m-help-form-3000"]').should(be.clickable).click()


@allure.step("Verify the standard sum message")
def check_standard_sum_message(int):
    if int == 300:
        browser.element('.form-donate__sum--desc active').should(have.text(THREE_HUNDRED_MESSAGE))
    elif int == 700:
        browser.element('.form-donate__sum--desc active').should(have.text(SEVEN_HUNDRED_MESSAGE))
    elif int == 1000:
        browser.element('.form-donate__sum--desc active').should(have.text(ONE_THOUSAND_MESSAGE))
    elif int == 3000:
        browser.element('.form-donate__sum--desc active').should(have.text(THREE_THOUSAND_MESSAGE))


@allure.step("Set a valid username into a donate form")
def set_username():
    browser.element('[name="help-transfer-name"]').set_value("Test_name")
    browser.element('[name="help-transfer-name"]').should(have.text("Test_name"))


@allure.step("Set a valid email into a donate form")
def set_email():
    browser.element('[name="help-transfer-email"]').set_value("test@test.com")
    browser.element('[name="help-transfer-name"]').should(have.text("test@test.com"))


@allure.step("Check the submit button is clickable")
def check_submit_button():
    browser.element('[type="submit"]').should(be.clickable)


@allure.step("CLick on submit button")
def click_on_submit_button():
    browser.element('[type="submit"]').click()
