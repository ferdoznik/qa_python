import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def set_browser_resolution():
    browser.config.window_height = 1080
    browser.config.window_width = 1700


@pytest.fixture()
def open_url():
    browser.open('https://google.com')


def test_google_search(set_browser_resolution, open_url):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="rso"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_random_input_search(set_browser_resolution, open_url):
    browser.element('[name="q"]').should(be.blank).type('askjdgqiuwehq').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
