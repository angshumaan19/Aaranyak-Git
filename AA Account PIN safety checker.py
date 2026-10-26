class Account:
    def __init__(self,owner,pin):
        self.owner = owner
        self.__pin = pin

    def show_pin_status(self):
        print("owner name :",self.owner)
        print("Pin is safely hidden inside the class")

    def check_pin(self,entered_pin):
        if entered_pin == self.__pin:
            print("access granted")
        else:
            print("access denied")

    def set_pin(self,new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("Pin changed successfully.")
        else:
            print("Invalid pin.Your new pin is not exactly 4 digits.")


    def __str__(self):
        return "Account holder:" + self.owner

my_account = Account("Aaranyak","2517")

print(my_account)

my_account.pin = "9999"
print("Tried changing pin directly from the outside.")

my_account.check_pin("9999")
my_account.check_pin("2517")

my_account.set_pin("2834")

my_account.check_pin("2834")