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
