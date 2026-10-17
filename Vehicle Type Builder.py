class Vehicle:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print(f"brand : {self.brand}")
        print(f"max speed : {self.max_speed}")

class Car(Vehicle):
    def __init__(self, name, color, brand, max_speed):
        self.name = name
        self.color = color
        super().__init__(brand, max_speed)

    def show_details(self):
        print(f"name : {self.name}")
        print(f"color : {self.color}")
        super().show_details()

    def fuel_type(self,fuel):
        print(self.name,"is",fuel,"fuel")

car = Car("tesla roadster 2","golden","tesla","300 k/ph")

car.show_details()
car.fuel_type("electric")

print("Is Vehicle a subclass of Car? :",issubclass(Car,Vehicle))