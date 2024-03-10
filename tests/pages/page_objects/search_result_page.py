from ..locators.search_result_page_locators import SearchResultPageLocators


class SearchResultPage:
    def __init__(self, page):
        self.page = page
        self.result_items_elements = self.page.locator(SearchResultPageLocators.RESULT_ITEMS_LOCATORS).all()
        self.menu_daily_weather_element = self.page.locator(SearchResultPageLocators.MENU_DAILY_WEATHER)

    def navigate_to_result_item_detail(self, index):
        self.result_items_elements[index].click()

    def navigate_to_daily_weather(self):
        self.menu_daily_weather_element.click()

