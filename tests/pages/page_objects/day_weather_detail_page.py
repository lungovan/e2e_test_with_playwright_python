from tests.pages.locators.day_weather_detail_page_locator import DayWeatherDetailLocators
from tests.utils.temperature_helper import format_real_feel_temperature, format_temperature


class DayWeatherDetailPage:
    def __init__(self, page):
        self.page = page

    def get_weather_data(self):

        temperature = self.page.locator(DayWeatherDetailLocators.TEMPERATURE).inner_text()
        temperature = format_temperature(temperature)

        temperature_real_feel = self.page.locator(DayWeatherDetailLocators.REAL_FEEL).inner_text()
        temperature_real_feel = format_real_feel_temperature(temperature_real_feel)

        main_weather = self.page.locator(DayWeatherDetailLocators.MAIN_WEATHER).inner_text()

        humidity = self.page.locator(DayWeatherDetailLocators.HUMIDITY).inner_text()

        data = {"temperature": temperature,
                "temperature_real_feel": temperature_real_feel,
                "main_weather": main_weather,
                "humidity": humidity
                }

        return data
