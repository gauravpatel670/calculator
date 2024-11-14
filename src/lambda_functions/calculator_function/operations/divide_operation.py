class DivideOperation:
    def execute(self, first_number, second_number):
        if first_number is None or second_number is None:
            raise ValueError("Both numbers are required")
        if second_number == 0:
            raise ValueError("Division by zero is not allowed")
        return first_number / second_number
