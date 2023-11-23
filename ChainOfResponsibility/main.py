from Handlers import *

if __name__ == "__main__":
    calculator = Calculator()

    request_add = Request(operation='add', num1=5, num2=3)
    request_subtract = Request(operation='subtract', num1=8, num2=4)
    request_multiply = Request(operation='multiply', num1=6, num2=2)
    request_divide = Request(operation='divide', num1=10, num2=2)

    calculator.perform_operation(request_add)
    calculator.perform_operation(request_subtract)
    calculator.perform_operation(request_multiply)
    calculator.perform_operation(request_divide)