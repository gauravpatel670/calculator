import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler


def test_multiply():
    event = {
        "operation": "multiply",
        "first_number": 4,
        "second_number": 3
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 200  # Check for success status code
    assert result["body"]["result"] == 130  # Check for correct multiplication result
