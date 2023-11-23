from Mediator import ATCControlTower, AirbusA320, Boeing737

if __name__ == "__main__":
    control_tower = ATCControlTower()

    airbus_a320_1 = AirbusA320("A320-001")
    airbus_a320_2 = AirbusA320("A320-002")
    boeing_737_1 = Boeing737("737-001")

    control_tower.register_plane(airbus_a320_1)
    control_tower.register_plane(airbus_a320_2)
    control_tower.register_plane(boeing_737_1)

    airbus_a320_1.send_message("Hello, this is Airbus A320-001. Requesting landing clearance.")
    boeing_737_1.send_message("Greetings, this is Boeing 737-001. Currently in holding pattern.")