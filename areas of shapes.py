import math
class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method!")

class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

r = rectangle(23,34)
c = circle(45)

shapes = [r,c]

for shaped in shapes:
    print(f"The area is : {shaped.area():.2f}")