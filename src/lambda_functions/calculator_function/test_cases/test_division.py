import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler


def test_division():
    event = {
        "operation": "divide",
        "first_number": 6,
        "second_number": 2
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 200  # Check for success status code
    assert result["body"]["result"] == 3  # Check for correct division result


def test_divide_by_zero():
    event = {
        "operation": "divide",
        "first_number": 5,
        "second_number": 0
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 400  # Check for error status code
    assert "Division by zero" in result["body"]["error"]  # Check for division by zero error message


def test_divide_with_missing_second_number():
    event = {
        "operation": "divide",
        "first_number": 2,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required"

def test_divide_with_missing_first_number():
    event = {
        "operation": "divide",
        "first_number": None,
        "second_number": 2
    }

    result = lambda_handler(event, None)
    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required"

def test_divide_with_missing_both_number():
    event = {
        "operation": "divide",
        "first_number": None,
        "second_number": None
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Both numbers are required"