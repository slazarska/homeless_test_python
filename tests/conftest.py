
import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 2560
    browser.config.window_height = 1440
    yield
    browser.quit()
