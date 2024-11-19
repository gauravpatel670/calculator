import pytest
from src.lambda_functions.greetings_function.lambda_function import lambda_handler

def test_greet_person():
    event = {
        "first_name": "John",
        "last_name": "Doe"
    }
    result = lambda_handler(event, None)
    assert result["statusCode"] == 2000
    assert result["body"]["message"] == "Hello, John Doe! Welcome!"

def test_missing_first_name():
    event = {
        "last_name": "Doe"
    }
    result = lambda_handler(event, None)
    assert result["statusCode"] == 4000
    assert "error" in result["body"]

def test_missing_last_name():
    event = {
        "first_name": "John"
    }
    result = lambda_handler(event, None)
    assert result["statusCode"] == 4000
    assert "error" in result["body"]
