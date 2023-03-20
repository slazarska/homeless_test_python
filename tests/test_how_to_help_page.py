from homeless_test_python import app
import allure
from allure_commons.types import Severity


@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("A regular donation")
@allure.description("Test checks that the default state of donation is regular")
def test_choose_default_state_of_donation(how_to_help):
    app.howtohelp.check_donation_warning(app.howtohelp.REGULAR)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("One-time donation")
@allure.description("Test checks the choice a one-time donation and verifies the one-time payment methods")
def test_choose_of_one_time_donation(how_to_help):
    app.howtohelp.choose_one_time_donation()
    app.howtohelp.check_donation_warning(app.howtohelp.ONE_TIME)
    '''
    add the check of payments methods
    '''


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("A regular donation")
@allure.description("Test checks the choice a regular donation and verifies the regular payment methods")
def test_choose_regular_donation(how_to_help):
    app.howtohelp.choose_regular_donation()
    app.howtohelp.check_donation_warning(app.howtohelp.REGULAR)
    '''
    add the check of payments methods
    '''


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("A regular donation")
@allure.description("Test checks the choice of donation amount for the regular donation")
def test_choose_sum_of_regular_donation(how_to_help):
    app.howtohelp.choose_regular_donation()
    app.howtohelp.choose_standard_sum_help(300)
    app.howtohelp.check_standard_sum_message(300)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("One-time donation")
@allure.description("Test checks the choice of donation amount for the one-time donation")
def test_choose_sum_of_one_time_donation(how_to_help):
    app.howtohelp.choose_one_time_donation()
    app.howtohelp.choose_standard_sum_help(1000)
    app.howtohelp.check_standard_sum_message(1000)


@allure.severity(Severity.CRITICAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("Donate Form")
@allure.description("Tests checks the filling the field into a donate form with valid data,"
                    "checks for absence of error messages and check that submit button is clickable")
def test_fill_the_donate_form_with_valid_data(how_to_help):
    app.howtohelp.set_username()
    app.howtohelp.set_email()
    app.howtohelp.check_submit_button()


@allure.severity(Severity.NORMAL)
@allure.label("owner", "slazarska")
@allure.feature("Donation")
@allure.story("Donate Form")
@allure.description("Test checks that the required fields into a donate form must be filled "
                    "and checks an error message")
def test_fill_the_donate_form_with_valid_data(how_to_help):
    app.howtohelp.set_username()
    app.howtohelp.check_submit_button()
