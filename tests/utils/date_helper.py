import datetime

DAY_OF_WEEK = {
    "SUN": "Sunday",
    "MON": "Monday",
    "TUE": "Tuesday",
    "WED": "Wednesday",
    "THU": "Thursday",
    "FRI": "Friday",
    "SAT": "Saturday"
}


def format_date(day_of_week: str, date_and_month: str) -> str:
    """
    Format date string to expected format

    :param day_of_week: str
    :param date_and_month: str
    :return: str
        Example: Saturday, March 9
    """
    month_number, day = date_and_month.split("/")
    month = datetime.date(1900, int(month_number), 1).strftime('%B')

    return DAY_OF_WEEK[day_of_week] + ", " + month + " " + day


def get_current_time_str():
    """
    Get current time in string with format of %Y%m%d-%H%M
    :return: str
        Example: 20240310-0831
    """
    return datetime.datetime.now().strftime('%Y%m%d-%H%M')
