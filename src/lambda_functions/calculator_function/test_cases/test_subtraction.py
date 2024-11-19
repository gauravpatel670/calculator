import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler


def test_subtraction():
    event = {
        "operation": "subtract",
        "first_number": 5,
        "second_number": 3
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 2000  # Check for success status code
    assert result["body"]["result"] == 2  # Check for correct result


def test_subtraction_with_missing_second_number():
    event = {
        "operation": "subtract",
        "first_number": 2,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 4000
    assert result["body"]["error"] == "Both numbers are required for this operation."

def test_subtraction_with_missing_first_number():
    event = {
        "operation": "subtract",
        "first_number": None,
        "second_number": 2
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 4000
    assert result["body"]["error"] == "Both numbers are required for this operation."

def test_subtraction_with_missing_both_number():
    event = {
        "operation": "subtract",
        "first_number": None,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 4000
    assert result["body"]["error"] == "Both numbers are required for this operation."