class IO_string:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = str(input("Enter a string : "))
    def print_string(self):
        print("uppercase string:",self.str1.upper())

str1 = IO_string()
str1.get_string()
str1.print_string()