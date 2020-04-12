import pytest
from paranuara_challenge.utils.input_validator import validate_input_args
from paranuara_challenge.exceptions.InputException import InvalidInputException


def test_validate_input_args_throws_exception_for_non_allowed_characters():
    arg_value = 'Invalida$arg$value'
    with pytest.raises(InvalidInputException) as exc_info:
        validate_input_args(arg_value)
    assert f'Input value: {arg_value} does not match expected pattern and is not alphanumeric' == str(exc_info.value)


def test_validate_input_args_throws_excpetion_for_strings_exceeding_max_length():
    arg_value = 'x' * 256
    with pytest.raises(InvalidInputException) as exc_info:
        validate_input_args(arg_value)
    assert f'input value: {arg_value} exceeds allowed length of 255 characters' == str(exc_info.value)


def test_validate_input_args_handles_multiple_values():
    arg_values = ['abc', 'x' * 256]
    with pytest.raises(InvalidInputException) as exc_info:
        validate_input_args(*arg_values)
    assert f'input value: {arg_values[1]} exceeds allowed length of 255 characters' == str(exc_info.value)
