import allure
from selene.support.shared import browser
from selene import be, have


@allure.step("Choose_period_help")
def choose_period_help():
    browser.element('[data-period="разово"]').should(be.clickable).click()


@allure.step("Check choosed help period")
def check_period_help():
    browser.element('.donation-warning').should(have.text("Вы выбрали разовое пожертвование"))


@allure.step("Open Main Page")
def choose_sum_help():
    browser.element('[label="m-help-form-300"]').should(be.clickable).click()


@allure.step("Open Main Page")
def check_choosed_sum_help():
    browser.element('.form-donate__sum--desc active')\
        .should(have.text("300 рублей позволят одному человеку переночевать в Ночном приюте"))


@allure.step("Open Main Page")
def choose_sum_help():
    browser.element('[name="help-transfer-name"]').set_value("Test_name")
    browser.element('[name="help-transfer-name"]').should(have.text("Test_name"))


@allure.step("Open Main Page")
def choose_sum_help():
    browser.element('[name="help-transfer-email"]').set_value("test@test.com")
    browser.element('[name="help-transfer-name"]').should(have.text("test@test.com"))


@allure.step("CLick on submit button")
def click_on_submit_button():
    browser.element('[type="submit"]').should(be.clickable).click()







