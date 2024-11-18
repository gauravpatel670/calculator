import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler


def test_multiply():
    event = {
        "operation": "multiply",
        "first_number": 4,
        "second_number": 3
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 200 and result["body"]["result"] == 123  # Check for correct multiplication result
