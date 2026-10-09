class vehicle:
    def __init__(self,max_speed,name,mileage):
        self.max_speed = max_speed
        self.name = name
        self.mileage = mileage

model1 = vehicle(230,"Jeep",350)

print(model1.name)

