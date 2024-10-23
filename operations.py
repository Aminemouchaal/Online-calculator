from exceptions import DivisionByZeroError, InvalidOperationError, InvalidInputError

def validate_numbers(num1: str, num2: str) -> tuple[float, float]:
    """Validate and convert input strings to numbers"""
    try:
        n1 = float(num1)
        n2 = float(num2)
        return n1, n2
    except ValueError:
        raise InvalidInputError()

def perform_operation(operation: str, num1: str, num2: str) -> float:
    """
    Performs the specified mathematical operation on two numbers
    Args:
        operation (str): The operation to perform (add/subtract/multiply/divide)
        num1 (str): First number as string
        num2 (str): Second number as string
    Returns:
        float: Result of the operation
    Raises:
        InvalidOperationError: If operation is not supported
        DivisionByZeroError: If attempting to divide by zero
        InvalidInputError: If inputs are not valid numbers
    """
    # Validate and convert inputs
    n1, n2 = validate_numbers(num1, num2)
    
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(DivisionByZeroError())
    }
    
    if operation not in operations:
        raise InvalidOperationError(f"Invalid operation. Valid operations are: {', '.join(operations.keys())}")
    
    try:
        return operations[operation](n1, n2)
    except ZeroDivisionError:
        raise DivisionByZeroError()