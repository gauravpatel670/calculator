import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler


def test_subtraction():
    event = {
        "operation": "subtract",
        "first_number": 5,
        "second_number": 3
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 200  # Check for success status code
    assert result["body"]["result"] == 30  # Check for correct result
