# class Pet:
#     pass
from time import perf_counter


class Pet:
        print('=============================\nPET PROFILE BUILDER\n=============================')

pet_object = Pet()

class pet_profile:
    category = "pet"

    def __init__(self,name,animal_type,age,favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food

dan = pet_profile("dan","great dane",8,"bones")
woolly = pet_profile("woolly","pug",5,"snacks")

print("{} is a {}".format(dan.name,dan.animal_type))
print("{} is a {}".format(woolly.name,woolly.animal_type))

print("{}'s age is {} and his favourite food is {}".format(dan.name,dan.age,dan.favourite_food))
print("{}'s age is {} and his favourite food is {}".format(woolly.name,woolly.age,woolly.favourite_food))
