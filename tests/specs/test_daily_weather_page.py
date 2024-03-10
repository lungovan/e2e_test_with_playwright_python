from playwright.sync_api import expect
from tests.pages.locators.search_result_page_locators import SearchResultPageLocators
from tests.pages.page_objects.daily_weather_page import DailyWeatherPage
from tests.pages.page_objects.search_result_page import SearchResultPage
from tests.utils.temperature_helper import celsius_to_fahrenheit, TemperatureUnit


def test_daily_weather_temperatures_in_both_units_are_equal(browser_context, home_page, setting_page, logger):
    """

    :param browser_context:
    :param home_page:
    :param setting_page:
    :param logger:
    :return:
    """
    # Set unit to Celsius
    setting_page.set_display_unit(TemperatureUnit.Celsius)

    # Open Home page, search a location, navigate to Daily Weather Page
    # Get daily weather information in Celsius
    home_page.load()
    home_page.fill_search_input("District 1, Ho Chi Minh")
    home_page.submit_search()
    expect(home_page.page.locator(SearchResultPageLocators.SEARCH_RESULT_HEADING)).to_be_attached()
    search_result_page = SearchResultPage(home_page.get_page_instance())
    search_result_page.navigate_to_result_item_detail(1)
    search_result_page.page.mouse.click(100, 200)
    search_result_page.navigate_to_daily_weather()
    daily_weather_page = DailyWeatherPage(search_result_page.page)
    dates_title = daily_weather_page.get_dates_title()
    url = daily_weather_page.page.url
    data_in_c = daily_weather_page.get_daily_data()

    # Save weather information to log file
    logger.logger.info(dates_title + " In Celsius " + str(data_in_c))

    # Set unit to Fahrenheit
    setting_page.load()
    setting_page.set_display_unit(TemperatureUnit.Fahrenheit)

    # Open Daily Weather Page again
    # Get daily weather information in Fahrenheit
    daily_weather_page.page.goto(url)
    data_in_f = daily_weather_page.get_daily_data()

    # Save weather information to log file
    logger.logger.info(dates_title + " In Fahrenheit " + str(data_in_f))

    # Compare temperature values in Celsius and temperature values in Fahrenheit
    result = daily_weather_page.validate_temperature_in_celsius_and_fahrenheit(data_in_c, data_in_f, logger)

    assert result, "The variable should be True"
