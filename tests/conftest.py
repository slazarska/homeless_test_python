import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from homeless_test_python.utils import attach

DEFAULT_BROWSER = 'chrome'
DEFAULT_BROWSER_VERSION = '98.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        default=DEFAULT_BROWSER,
        help='web: browser (chrome | firefox | orepa| safari)'
    )

    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
        help='web: browser version (chrome: 100.0; if  firefox: 98.0)'
    )


@pytest.fixture(scope='session')
def get_option_browser_name(request):
    return request.config.getoption('--browser_name')


@pytest.fixture(scope='session')
def get_option_browser_version(request):
    return request.config.getoption('--browser_version')


@pytest.fixture(autouse=True)
def browser_management(get_option_browser_name, get_option_browser_version):
    browser_name = get_option_browser_name
    browser_name = browser_name if browser_name != '' else DEFAULT_BROWSER

    browser_version = get_option_browser_version
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function')
def how_to_help():
    browser.open('https://homeless.ru/how_to_help/')
