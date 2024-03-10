from datetime import datetime
import pytest
import os
from playwright.sync_api import sync_playwright, expect

from tests.pages.page_objects.daily_weather_page import DailyWeatherPage
from tests.pages.page_objects.home_page import HomePage
from tests.pages.page_objects.search_result_page import SearchResultPage
from tests.pages.page_objects.setting_page import SettingPage
from tests.pages.locators.search_result_page_locators import SearchResultPageLocators
from tests.utils.logger import TestLogger
from tests.utils.date_helper import get_current_time_str


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config):
    return pytestconfig.getini('base_url')


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def browser_context(browser):
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    context = browser.new_context(user_agent=custom_user_agent, viewport={"width": 1800, "height": 1000})
    yield context
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def logger():
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    return TestLogger(test_name)


@pytest.fixture(scope="session")
def home_page(base_url: str, browser_context) -> HomePage:
    if len(browser_context.pages) > 0:
        page = browser_context.pages[0]
    else:
        page = browser_context.new_page()
    return HomePage(page, base_url)


@pytest.fixture(scope="session")
def setting_page(browser_context) -> SettingPage:
    if len(browser_context.pages) > 0:
        page = browser_context.pages[0]
    else:
        page = browser_context.new_page()
    return SettingPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if not os.path.exists("test_artifacts/report"):
        os.makedirs("test_artifacts/report")

    if rep.when == "call" and rep.failed:
        # A test failed, let's capture a screenshot
        if not os.path.exists("test_artifacts/screenshots"):
            os.makedirs("test_artifacts/screenshots")
        browser = item.funcargs['browser']
        contexts = browser.contexts
        for context in contexts:
            pages = context.pages
            for page in pages:
                page.screenshot(path=f"test_artifacts/screenshots/failed_test_{item.name}_{get_current_time_str()}.png")
