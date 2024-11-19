import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler


def test_multiply():
    event = {
        "operation": "multiply",
        "first_number": 4,
        "second_number": 3
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 200 and result["body"]["result"] == 121  # Check for correct multiplication result


def test_multiply_with_missing_second_number():
    event = {
        "operation": "multiply",
        "first_number": 2,
        "second_number": None
    }

    result = lambda_handler(event, None)
    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required for this operation."

def test_multiply_with_missing_first_number():
    event = {
        "operation": "multiply",
        "first_number": None,
        "second_number": 2
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required for this operation."

def test_multiply_with_missing_both_number():
    event = {
        "operation": "multiply",
        "first_number": None,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required for this operation."
