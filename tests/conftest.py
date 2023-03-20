import pytest
from selene.support.shared import browser
from homeless_test_python import app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser_management():
    browser.config.window_width = 2560
    browser.config.window_height = 1440

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    #driver = webdriver.Remote(
    #    command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
   #     options=options)

    #browser.config.driver = driver

    yield

    #app.attach.add_html(browser)
    #app.attach.add_screenshot(browser)
    #app.attach.add_logs(browser)
    #app.attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function')
def how_to_help(browser_management):
    browser.open('https://homeless.ru/how_to_help/')
