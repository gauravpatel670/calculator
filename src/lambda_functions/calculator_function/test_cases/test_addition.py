import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler

def test_addition_with_two_numbers():
    event = {
        "operation": "add",
        "first_number": 2,
        "second_number": 3
    }
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert result["body"]["result"] == 5


def test_addition_with_missing_second_number():
    event = {
        "operation": "add",
        "first_number": 2,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required"

def test_addition_with_missing_first_number():
    event = {
        "operation": "add",
        "first_number": None,
        "second_number": 2
    }

    result = lambda_handler(event, None)
    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required"

def test_addition_with_missing_both_number():
    event = {
        "operation": "add",
        "first_number": None,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required"
