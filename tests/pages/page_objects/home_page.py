from playwright.sync_api import Page, expect
from ..locators.home_page_locators import HomeBaseLocators
from ..locators.search_result_page_locators import SearchResultPageLocators


class HomePage:

    PAGE_TITLE = "Local, National, & Global Daily Weather Forecast | AccuWeather"

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.url = base_url
        self.search_input_element = self.page.locator(HomeBaseLocators.SEARCH_INPUT_LOCATOR)
        self.search_icon_element = self.page.locator(HomeBaseLocators.SEARCH_ICON_LOCATOR)

    def load(self):
        self.page.goto(self.url)

    def fill_search_input(self, text):
        self.search_input_element.fill(text)

    def submit_search(self):
        self.search_icon_element.click()
        expect(self.page.locator(SearchResultPageLocators.SEARCH_RESULT_HEADING)).to_be_attached()

    def get_page_instance(self) -> Page:
        return self.page
