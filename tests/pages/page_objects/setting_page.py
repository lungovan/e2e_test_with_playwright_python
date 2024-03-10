from tests.pages.locators.setting_page_locators import SettingPageLocators


class SettingPage:
    URL = "https://www.accuweather.com/en/settings"

    def __init__(self, page):
        self.page = page
        self.unit_select_element = self.page.locator(SettingPageLocators.UNIT_SELECT)
        self.load()

    def load(self):
        self.page.goto(self.URL)

    def set_display_unit(self, value) -> None:
        """
        The function is for switch the display unit. If the current unit is Celsius, switch to Fahrenheit and reversed.
        :return:
        """
        self.unit_select_element.select_option(value)

    def get_display_unit(self) -> str:
        """

        :return:
        """
        current_value = self.unit_select_element.evaluate('(element) => element.options[element.selectedIndex].value')
        return current_value
