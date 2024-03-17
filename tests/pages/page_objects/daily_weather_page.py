from tests.pages.locators.daily_weather_locators import DailyWeatherLocators
from tests.pages.locators.search_result_page_locators import SearchResultPageLocators
from tests.pages.page_objects.day_weather_detail_page import DayWeatherDetailPage
from tests.pages.page_objects.home_page import HomePage
from tests.pages.page_objects.search_result_page import SearchResultPage
from tests.utils.logger import TestLogger
from tests.utils.date_helper import format_date
from tests.utils.temperature_helper import format_temperature, format_real_feel_temperature
from playwright.sync_api import expect
from tests.utils.temperature_helper import celsius_to_fahrenheit
from playwright.sync_api import sync_playwright
import queue
import concurrent.futures


class DailyWeatherPage:
    def __init__(self, page):
        self.page = page
        self.dates_title_element = self.page.locator(DailyWeatherLocators.DAILY_TITLE)
        self.date_weather_cards = self.page.locator(DailyWeatherLocators.DAY_WEATHER_CARD).all()

    def get_dates_title(self):
        return self.dates_title_element.inner_text()

    # def get_daily_data(self) -> list:
    #     """
    #     Get a list of weather information for all days that listed on the page.
    #     :return: list
    #     """
    #     return_data = []
    #
    #     for date_weather_card in self.date_weather_cards:
    #
    #         day_of_week = date_weather_card.locator(DailyWeatherLocators.DATE).inner_text()
    #         day_and_month = date_weather_card.locator(DailyWeatherLocators.DATE2).inner_text()
    #
    #         temperature_high = date_weather_card.locator(DailyWeatherLocators.TEMP_HIGH).inner_text()
    #         temperature_low = date_weather_card.locator(DailyWeatherLocators.TEMP_LOW).inner_text()
    #         temperature_high = format_temperature(temperature_high)
    #         temperature_low = format_temperature(temperature_low)
    #
    #         temperature_real_feel = date_weather_card.locator(DailyWeatherLocators.REAL_FEEL).all()[0].inner_text()
    #         temperature_real_feel = format_real_feel_temperature(temperature_real_feel)
    #
    #         date = format_date(day_of_week, day_and_month)
    #         main_weather = date_weather_card.locator(DailyWeatherLocators.MAIN_WEATHER).inner_text()
    #
    #         each_date_weather = {"date": date, "temperature_high": temperature_high,
    #                              "temperature_low": temperature_low, "temperature_real_feel": temperature_real_feel,
    #                              "main_weather": main_weather}
    #
    #         return_data.append(each_date_weather)
    #
    #     return return_data

    def get_daily_data(self, number_of_day=16) -> list:
        """
        Get a list of weather information for all days that listed on the page.
        :return: list
        """
        return_data = []

        # Get list of dates
        day_index = 1
        dates = []
        for date_weather_card in self.date_weather_cards:
            if day_index > number_of_day:
                break
            day_of_week = date_weather_card.locator(DailyWeatherLocators.DATE_OF_WEEK).inner_text()
            day_and_month = date_weather_card.locator(DailyWeatherLocators.DATE_WITH_MONTH).inner_text()
            date = format_date(day_of_week, day_and_month)
            dates.append(date)
            day_index = day_index + 1

        location_id = self.page.url.split("/")[-1]
        url_base = self.page.url.split(location_id)[0]
        day_segments = ["morning", "evening"]
        # Go to each date's weather detail pages to get ìnformation
        # https://www.accuweather.com/en/vn/ho-chi-minh-city/353981/daily-weather-forecast/353981
        # https://www.accuweather.com/en/vn/ho-chi-minh-city/353981/morning-weather-forecast/353981?day=1

        return_data = []

        # [{'Sunday, March 17': {'morning': {'temperature': '35', 'temperature_real_feel': 'RealFeel® 40°',
        #                                    'main_weather': 'Partly sunny and warm', 'humidity': '59%'},
        #                        'evening': {'temperature': '27', 'temperature_real_feel': 'RealFeel® 31°',
        #                                    'main_weather': 'Clear', 'humidity': '74%'}}}
        # ]

        day_index = 1
        for date in range(number_of_day):
            date_str = dates[day_index - 1]
            date_dict = {f"{date_str}": {}}
            for day_segment in day_segments:
                segment_dict = {f"{day_segment}": {}}
                day_url_weather = f"{url_base}{location_id}/{day_segment}-weather-forecast/{location_id}?day={day_index}"

                self.page.goto(day_url_weather)
                day_weather_detail_page = DayWeatherDetailPage(self.page)
                data = day_weather_detail_page.get_weather_data()

                segment_dict[f"{day_segment}"] = data
                date_dict[f"{date_str}"].update(segment_dict)

            return_data.append(date_dict)
            day_index = day_index + 1

        return return_data
