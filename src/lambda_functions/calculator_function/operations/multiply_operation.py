class MultiplyOperation:
    def execute(self, first_number, second_number):
        if first_number is None or second_number is None:
            raise ValueError("Both numbers are required for this operation.")
        return first_number * second_number
