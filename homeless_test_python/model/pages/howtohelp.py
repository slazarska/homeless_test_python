import allure
from selene.support.shared import browser
from selene import be, have
from homeless_test_python import app


ONE_TIME = 'one-time'
REGULAR = 'regular'


@allure.step("Choose one-time period help")
def choose_one_time_donation():
    browser.element('[data-period="разово"]').should(be.clickable).click()


@allure.step("Choose a regular period help")
def choose_regular_donation():
    browser.element('[data-period="ежемесячно"]').should(be.clickable).click()


@allure.step("Check choosed help period")
def check_donation_warning(period='text'):
    if period == ONE_TIME:
        browser.element('.donation-warning').should(have.text(app.Messages.ONE_TIME_DONATION_WARNING))
    elif period == REGULAR:
        browser.element('.donation-warning').should(have.text(app.Messages.REGULAR_DONATION_WARNING))


@allure.step("Choose the standard amount for the donation")
def choose_standard_sum_help(amount=int):
    if amount == 300:
        browser.element('[label="m-help-form-300"]').should(be.clickable).click()
    elif amount == 700:
        browser.element('[label="m-help-form-700"]').should(be.clickable).click()
    elif amount == 1000:
        browser.element('[label="m-help-form-1000"]').should(be.clickable).click()
    elif amount == 3000:
        browser.element('[label="m-help-form-3000"]').should(be.clickable).click()


@allure.step("Verify the standard sum message")
def check_standard_sum_message(amount=int):
    if amount == 300:
        browser.element('.form-donate__sum--desc active')\
            .should(have.text(app.Messages.THREE_HUNDRED_MESSAGE))
    elif amount == 700:
        browser.element('.form-donate__sum--desc active')\
            .should(have.text(app.Messages.SEVEN_HUNDRED_MESSAGE))
    elif amount == 1000:
        browser.element('.form-donate__sum--desc active')\
            .should(have.text(app.Messages.ONE_THOUSAND_MESSAGE))
    elif amount == 3000:
        browser.element('.form-donate__sum--desc active')\
            .should(have.text(app.Messages.THREE_THOUSAND_MESSAGE))


@allure.step("Set a valid username into a donate form")
def set_username(test_data='text'):
    app.Field.input_value(browser.element('[name="help-transfer-name"]'), test_data)
    #browser.element().set_value("Test_name").press_tab() #press_enter
    #browser.element('[name="help-transfer-name"]').should(have.text("Test_name"))


@allure.step("Set a valid email into a donate form")
def set_email(test_data='text'):
    app.Field.input_value(browser.element('[name="help-transfer-email"]'), test_data)
    #browser.element('[name=""]').set_value("test@test.com").press_tab()
    #browser.element('[name="help-transfer-name"]').should(have.text("test@test.com"))


@allure.step("Check the submit button is clickable")
def check_submit_button():
    browser.element('[type="submit"]').should(be.clickable)


@allure.step("Click on submit button")
def click_on_submit_button():
    browser.element('[type="submit"]').click()
