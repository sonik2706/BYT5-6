class Car:
    def __init__(self, model, color, year, engine, transmission, gps=False, leather_seats=False, body_kit=False, sport_exhausts_system=False):
        self.model = model
        self.color = color
        self.year = year
        self.engine = engine
        self.transmission = transmission
        self.gps = gps
        self.leather_seats = leather_seats
        self.body_kit = body_kit
        self.sport_exhausts_system = sport_exhausts_system

    def __str__(self):
        features = [
            f"Model: {self.model}",
            f"Color: {self.color}",
            f"Year: {self.year}",
            f"Engine: {self.engine}",
            f"Transmission: {self.transmission}",
            f"GPS: {self.gps}",
            f"Leather Seats: {self.leather_seats}"
        ]
        return "\n".join(features)

class CarBuilder:
    def __init__(self, *args, **kwargs):
        self.car = Car(*args, **kwargs)

    def add_gps(self):
        self.car.gps = True
        return self

    def add_leather_seats(self):
        self.car.leather_seats = True
        return self
    
    def add_body_kit(self):
        self.car.body_kit = True
        return self

    def add_sport_exhausts_system(self):
        self.car.sport_exhausts_system = True
        return self

    def get_result(self):
        return self.car

class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_luxury_car(self):
        self.builder.add_gps().add_leather_seats()

    def build_sports_car(self):
        self.builder.add_gps().add_leather_seats().add_body_kit().add_sport_exhausts_system()