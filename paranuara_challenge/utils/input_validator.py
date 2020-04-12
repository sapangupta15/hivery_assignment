import re
from paranuara_challenge.exceptions.InputException import InvalidInputException


def validate_input_args(*args):
    """
    validate that all query params contain only alphanumeric or whitespace characters
    and have length less than 255
    :param args:
    :return:
    """
    for arg in args:
        if not re.match(r'^[\w\-\s]+$', arg):
            raise InvalidInputException(f'Input value: {arg} does not match expected pattern and is not alphanumeric')
        if len(arg) > 255:
            raise InvalidInputException(f'input value: {arg} exceeds allowed length of 255 characters')
