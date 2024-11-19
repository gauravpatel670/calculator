import pytest
from src.lambda_functions.calculator_function.lambda_function import lambda_handler
def test_divide():
    event = {
        "operation": "dividethis",
        "first_number": 6,
        "second_number": 2
    }
    result = lambda_handler(event, None)

    assert result["statusCode"] == 400
    assert result["body"]["error"] == "Invalid operation. Supported operation_list are add, subtract, multiply, and divide."
