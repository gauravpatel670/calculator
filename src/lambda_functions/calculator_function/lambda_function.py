from src.lambda_functions.calculator_function.operations.add_operation import AddOperation
from src.lambda_functions.calculator_function.operations.subtract_operation import SubtractOperation
from src.lambda_functions.calculator_function.operations.multiply_operation import MultiplyOperation
from src.lambda_functions.calculator_function.operations.divide_operation import DivideOperation

def lambda_handler(event, context):
    # Get operation and numbers from the event
    operation = event.get("operation")
    first_number = event.get("first_number")
    second_number = event.get("second_number")

    # # Check if both numbers are provided
    # if first_number is None or second_number is None:
    #     return {
    #         "statusCode": 400,
    #         "body": {"error": "Both numbers are required"}
    #     }

    # Map operation_list to their corresponding classes
    operations = {
        "add": AddOperation(),
        "subtract": SubtractOperation(),
        "multiply": MultiplyOperation(),
        "divide": DivideOperation()
    }

    # Get the appropriate operation class
    operation_class = operations.get(operation)

    if not operation_class:
        return {
            "statusCode": 400,
            "body": {"error": "Invalid operation. Supported operation_list are add, subtract, multiply, and divide."}
        }

    # Execute the operation
    try:
        result = operation_class.execute(first_number, second_number)
        return {
            "statusCode": 200,
            "body": {"result": result}
        }
    except ValueError as e:
        return {
            "statusCode": 400,
            "body": {"error": str(e)}
        }

if __name__ == "__main__":
    # Create an example event to pass to the lambda_handler
    event = {
        "operation": "divide",
        "first_number": 5,
        "second_number": 2
    }

    # Context is not required for this basic example, so you can pass None
    context = None

    # Call the lambda_handler function with the event and context
    response = lambda_handler(event, context)

    # Print the response from the lambda_handler
    print(response)
