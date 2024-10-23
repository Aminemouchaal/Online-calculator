class DivisionByZeroError(Exception):
    """Custom exception for division by zero operations"""
    def __init__(self, message="Division by zero is not allowed"):
        self.message = message
        super().__init__(self.message)

class InvalidOperationError(Exception):
    """Custom exception for invalid calculator operations"""
    def __init__(self, message="Invalid operation"):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(Exception):
    """Custom exception for invalid input values"""
    def __init__(self, message="Invalid input: Please provide valid numbers"):
        self.message = message
        super().__init__(self.message)