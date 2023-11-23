from Car import *

if __name__ == "__main__":
    car_builder1 = CarBuilder(model="Limousine", color="Black", year=2023, engine="V6", transmission="Automatic")
    director = CarDirector(car_builder1)

    director.build_luxury_car()
    luxury_car = car_builder1.get_result()
    print("Luxury Car:")
    print(luxury_car)

    print("==============================")

    car_builder2 = CarBuilder(model="Coupe", color="Red", year=2023, engine="V8", transmission="Manual")
    director = CarDirector(car_builder2)

    sports_car = car_builder2.get_result()
    director.build_sports_car()
    print("Sports Car:")
    print(sports_car)