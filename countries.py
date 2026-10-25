class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is the most populated country.")


class USA():
    def capital(self):
        print("Washington D.C is the capital of USA.")
    def language(self):
        print("English(American) is the primary of USA.")
    def type(self):
        print("USA is the most strongest country.")


i = India()
u = USA()

for country in (i,u):
    country.capital()
    country.language()
    country.type()