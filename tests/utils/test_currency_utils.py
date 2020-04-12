from paranuara_challenge.utils.currency_utils import convert_currency_string_to_numeric, \
    convert_number_to_currency_value


def test_convert_currency_string_to_numeric_removes_dollar_and_thousand_separators():
    value = '$4,567.12'
    numeric_value = convert_currency_string_to_numeric(value)
    assert numeric_value == 4567.12


def test_convert_number_to_currency_symbol_appends_dollar_and_thousands_separator():
    value = 4567.12
    formatted_currency_value = convert_number_to_currency_value(value)
    assert formatted_currency_value == '$4,567.12'


def test_convert_number_to_currency_symbol_limits_to_two_deimal_places():
    value = 4567.123
    formatted_currency_value = convert_number_to_currency_value(value)
    assert formatted_currency_value == '$4,567.12'
