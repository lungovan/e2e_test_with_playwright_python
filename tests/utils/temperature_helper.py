import re
import math


class TemperatureUnit:
    Celsius = "C"
    Fahrenheit = "F"


def format_temperature(temp_str: str) -> str:
    """
    Format the temperature

    :param temp_str:
    :return: str
        Example: 37
    """
    return re.search(r'\d+', temp_str).group()


def format_real_feel_temperature(temp_str: str) -> str:
    """
    Format the Real feel temperature

    :param temp_str:
    :return: str
        Example: RealFeel®81°
    """
    return temp_str.replace("\n", "")


def celsius_to_fahrenheit(celsius_value: int) -> int:
    """
    Convert temperature in celsius unit to fahrenheit unit

    :param celsius_value:
    :return: integer
    """
    return math.floor(int(celsius_value) * 1.8) + 32


def validate_temperature_in_celsius_and_fahrenheit(data_in_c, data_in_f, logger) -> bool:
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

        for key in data_item.keys():

            each_day_data = data_item[key]

            for segment_key in each_day_data.keys():

                data = each_day_data[segment_key]
                temperature_in_c = data["temperature"]
                expected_temperature_high_in_f = celsius_to_fahrenheit(temperature_in_c)
                temperature_in_f = data_in_f[index][key][segment_key]["temperature"]

                if abs(int(temperature_in_f) - int(expected_temperature_high_in_f)) > 1:
                    result = False
                    logger.logger.info(f"Data discrepancy on date {key}. Temperature in C = {temperature_in_c}."
                                       f" Temperature in F = {temperature_in_f}. Expected temperature in F = "
                                       f"{expected_temperature_high_in_f}")

        index = index + 1

    return result
