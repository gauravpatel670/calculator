def lambda_handler(event, context):
    # Get the first and last name from the event
    first_name = event.get("first_name")
    last_name = event.get("last_name")

    # Validate that both parameters are provided
    if not first_name or not last_name:
        return {
            "statusCode": 400,
            "body": {
                "error": "Both 'first_name' and 'last_name' are required."
            }
        }

    # Generate the greeting message
    greeting = f"Hello, {first_name} {last_name}! Welcome!"

    # Return the greeting with a 200 status code
    return {
        "statusCode": 200,
        "body": {
            "message": greeting
        }
    }

