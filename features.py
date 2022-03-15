import json
import calendar

from datetime import datetime
from copy import copy
from collections import OrderedDict


def load_json(file_path: str) -> dict:

    with open(file_path, 'r') as file:
        return json.load(file)


def validate_date(date_str: str) -> datetime:
    """Converts string 'dd.mm.YY in the Python datettime object.
    Datetime instance also validates the string.

    Args:
        date_str (str): A string with the date in 'dd.mm.YY' format&

    Returns:
        datetime: Datetime instance.
    """

    try:
        return datetime.strptime(date_str, '%d.%m.%Y')
    except ValueError:
        raise


def add_months(sourcedate: datetime, months:int = 1) -> datetime:
    """This function adds a month to datetime Python instance

    Args:
        sourcedate (datetime): A datetime instance
        months (int, optional): _description_. Defaults to 1.
        Months to add

    Returns:
        _type_: Datetime instance with months added.
    """
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])

    return datetime(year, month, day)


def calc_amount(data: dict) -> OrderedDict:
    """This function calcs amount by the date

    Args:
        data (dict): Calc data dict {'date': 'dd.mm.YYY',
    'periods': int (1-60), 'amount': int (10 000 - 3 000 000),
    'rate': float (1-8)}

    Returns:
        OrderedDict: An OrderedDict with dates and amounts.
        {'date': amount, ...}
    """
    date_ = validate_date(data['date'])
    periods, amount, rate = data['periods'], data['amount'], data['rate']
    result = OrderedDict()

    cur_date = copy(date_)
    for i in range(periods):
        if i > 0:
            cur_date = add_months(date_, i)
        amount = round(amount * (1 + (rate / 12 / 100)), 2)
        result[cur_date.strftime('%d.%m.%Y')] = amount

    return result
