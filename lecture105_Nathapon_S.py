#การสืบทอดของโปรแกรม
class Vehicle:
    license_code = ""
    serial_code = ""
    face = ""
    def turn_on_air_conditioner(self):
        print("Turn On : Air")

class Cars(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Cars()
car1.turn_on_air_conditioner()
van1 = Van()
van1.turn_on_air_conditioner()
pick_up = PickUp()
pick_up .turn_on_air_conditioner()
estate_car = Estatecar()
estate_car.turn_on_air_conditioner()