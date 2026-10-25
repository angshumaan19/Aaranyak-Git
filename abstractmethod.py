from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")


class Fish(Animal):
    def move(self):
        print("I can swim")


class Snake(Animal):
    def move(self):
        print("I can slither and crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")

h = Human()
h.move()
f = Fish()
f.move()
s = Snake()
s.move()
d = Dog()
d.move()



