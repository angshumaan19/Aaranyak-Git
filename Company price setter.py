class Computer:
    def __init__(self):
        self.__max_price = 1000
    def sell(self):
        print("max price :",self.__max_price)
    def setMax_price(self,price):
        self.__max_price = price
c = Computer()
c.sell()
c.__max_price = 2000
c.sell()

c.setMax_price(2000)
c.sell()

