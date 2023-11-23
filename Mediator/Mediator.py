from abc import ABC, abstractmethod

class ATCMediator(ABC):
    @abstractmethod
    def register_plane(self, plane):
        pass

    @abstractmethod
    def send_message(self, sender, message):
        pass

class ATCControlTower(ATCMediator):
    def __init__(self):
        self.planes = []

    def register_plane(self, plane):
        if plane not in self.planes:
            self.planes.append(plane)
            plane.set_mediator(self)

    def send_message(self, sender, message):
        for plane in self.planes:
            if plane != sender:
                plane.receive_message(message)

class Plane(ABC):
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, message):
        pass

class AirbusA320(Plane):
    def send_message(self, message):
        print(f"Airbus A320 {self.registration_number} sends message: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"Airbus A320 {self.registration_number} receives message: {message}")

class Boeing737(Plane):
    def send_message(self, message):
        print(f"Boeing 737 {self.registration_number} sends message: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"Boeing 737 {self.registration_number} receives message: {message}")