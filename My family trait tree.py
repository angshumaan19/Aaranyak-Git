class Family_member:
    def __init__(self,eye_color,height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("eye color :",self.eye_color)
        print("height_cm :",self.height_cm)

class Kid(Family_member):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("name :",self.name)
        print("age :",self.age)
        super().show_traits()

    def favourite_hobby(self,hobby):
        print(self.name,"loves",hobby)


child = Kid("mark",9,"Blue",156)
child.show_traits()
child.favourite_hobby("cycling")

print("Is Kid a subclass of Family_member?",issubclass(Kid,Family_member))