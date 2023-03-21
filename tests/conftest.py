import pytest
from selene.support.shared import browser
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
    yield
    browser.quit()


'''
   driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
       options=options)

   browser.config.driver = driver

    yield

   attach.add_html(browser)
   attach.add_screenshot(browser)
    attach.add_logs(browser)
   attach.add_video(browser)
     browser.quit()
'''


@pytest.fixture(scope='function', autouse=True)
def how_to_help(browser_management):
    browser.open('https://homeless.ru/how_to_help/')
