from abc import ABC, abstractmethod

class OperationHandler(ABC):
    @abstractmethod
    def set_next(self, next_handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AdditionHandler(OperationHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler

        return next_handler

    def handle(self, request):
        if request.operation == 'add':
            result = request.num1 + request.num2
            print(f"{request.num1} + {request.num2} = {result}")
        elif self.next_handler:
            self.next_handler.handle(request)

class SubtractionHandler(OperationHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler

        return next_handler

    def handle(self, request):
        if request.operation == 'subtract':
            result = request.num1 - request.num2
            print(f"{request.num1} - {request.num2} = {result}")
        elif self.next_handler:
            self.next_handler.handle(request)

class MultiplicationHandler(OperationHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler

        return next_handler

    def handle(self, request):
        if request.operation == 'multiply':
            result = request.num1 * request.num2
            print(f"{request.num1} * {request.num2} = {result}")
        elif self.next_handler:
            self.next_handler.handle(request)

class DivisionHandler(OperationHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler

        return next_handler

    def handle(self, request):
        if request.operation == 'divide':
            if request.num2 != 0:
                result = request.num1 / request.num2
                print(f"{request.num1} / {request.num2} = {result}")
            else:
                print("Cannot divide by zero.")
        elif self.next_handler:
            self.next_handler.handle(request)

class Calculator:
    def __init__(self):
        self.handler_chain = AdditionHandler()
        self.handler_chain.set_next(SubtractionHandler()).set_next(MultiplicationHandler()).set_next(DivisionHandler())

    def perform_operation(self, request):
        self.handler_chain.handle(request)

class Request:
    def __init__(self, operation, num1, num2):
        self.operation = operation
        self.num1 = num1
        self.num2 = num2