from tests.pages.locators.daily_weather_locators import DailyWeatherLocators
from tests.pages.locators.search_result_page_locators import SearchResultPageLocators
from tests.pages.page_objects.home_page import HomePage
from tests.pages.page_objects.search_result_page import SearchResultPage
from tests.utils.logger import TestLogger
from tests.utils.date_helper import format_date
from tests.utils.temperature_helper import format_temperature, format_real_feel_temperature
from playwright.sync_api import expect
from tests.utils.temperature_helper import celsius_to_fahrenheit


class DailyWeatherPage:
    def __init__(self, page):
        self.page = page
        self.dates_title_element = self.page.locator(DailyWeatherLocators.DAILY_TITLE)
        self.date_weather_cards = self.page.locator(DailyWeatherLocators.DAY_WEATHER_CARD).all()

    def get_dates_title(self):
        return self.dates_title_element.inner_text()

    def get_daily_data(self) -> list:
        """
        Get a list of weather information for all days that listed on the page.
        :return: list
        """
        return_data = []
        for date_weather_card in self.date_weather_cards:

            day_of_week = date_weather_card.locator(DailyWeatherLocators.DATE).inner_text()
            day_and_month = date_weather_card.locator(DailyWeatherLocators.DATE2).inner_text()

            temperature_high = date_weather_card.locator(DailyWeatherLocators.TEMP_HIGH).inner_text()
            temperature_low = date_weather_card.locator(DailyWeatherLocators.TEMP_LOW).inner_text()
            temperature_high = format_temperature(temperature_high)
            temperature_low = format_temperature(temperature_low)

            temperature_real_feel = date_weather_card.locator(DailyWeatherLocators.REAL_FEEL).all()[0].inner_text()
            temperature_real_feel = format_real_feel_temperature(temperature_real_feel)

            date = format_date(day_of_week, day_and_month)
            main_weather = date_weather_card.locator(DailyWeatherLocators.MAIN_WEATHER).inner_text()

            each_date_weather = {"date": date, "temperature_high": temperature_high, "temperature_low": temperature_low,
                                 "temperature_real_feel": temperature_real_feel, "main_weather": main_weather}

            return_data.append(each_date_weather)

        return return_data

    def validate_temperature_in_celsius_and_fahrenheit(self, data_in_c, data_in_f, logger) -> bool:
        """

        :param data_in_c:
        :param data_in_f:
        :param logger:
        :return:
        """
        result = True
        if len(data_in_c) == 0 or len(data_in_f) == 0:
            result = False
        if len(data_in_c) != len(data_in_f):
            result = False

        index = 0
        for data_item in data_in_c:
            temperature_high = celsius_to_fahrenheit(data_item['temperature_high'])
            temperature_low = celsius_to_fahrenheit(data_item['temperature_low'])
            temperature_high_in_f = int(data_in_f[index]['temperature_high'])
            temperature_low_in_f = int(data_in_f[index]['temperature_low'])
            if temperature_high - temperature_high_in_f > 1 or temperature_low - temperature_low_in_f > 1:
                result = False
                logger.logger.info(data_item["date"])
                logger.logger.info("Temperature In Celsius:" + data_item['temperature_high'] + "/" +
                                   data_item['temperature_low'])
                logger.logger.info("Temperature In Fahrenheit:" + data_in_f[index]['temperature_high'] + "/" +
                                   data_in_f[index]['temperature_low'])
                logger.logger.info("Temperature In Fahrenheit Should Be:" +
                                   str(celsius_to_fahrenheit(data_item['temperature_high'])) + "/" +
                                   str(celsius_to_fahrenheit(data_item['temperature_low'])))

            index = index + 1

        return result

