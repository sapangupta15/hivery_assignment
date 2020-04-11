import locale


def convert_currency_string_to_numeric(value):
    """
    replace currency symbol, thousands separator
    :param value:
    :return:
    """
    return value[1:].replace(',', '')


def convert_number_to_currency_value(value):
    """
    Convert given numeric value to string with thousands separator and have upto 2 decimal places
    Also, add $ currency sign in front of the value
    :param value:
    :return:
    """
    locale.setlocale(locale.LC_ALL, '')
    return "${:,.2f}".format(value)
