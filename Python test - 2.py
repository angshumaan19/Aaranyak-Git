def add(a,b):
    try:
        return a + b
    except ValueError:
        print("dont enter letters instead of numbers!")
        return None

def subtract(a,b):
    try:
        return a - b
    except ValueError:
        print("dont enter letters instead of numbers!")
        return None

def multiply(a,b):
    try:
        return a * b
    except ValueError:
        print("dont enter letters instead of numbers!")
        return None

def divide(a,b):
    try:
        return a / b
    except ValueError:
        print("dont enter letters instead of numbers!")
        return None
    except ZeroDivisionError:
        print("dividing by zero is an error!")
        return None

print(add(float(input("enter a number")),float(input("enter another number"))))
print(subtract(float(input("enter a number")),float(input("enter another number"))))
print(multiply(float(input("enter a number")),float(input("enter another number"))))
print(divide(float(input("enter a number")),float(input("enter another number"))))
