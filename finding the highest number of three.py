x=int(input("enter first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))


print(x,y,z)

def highest_number(x,y,z):
    if z < x > y:
        print(f"{x} is the biggest")

    elif x < z > y:
        print(f"{z} is the biggest")

    elif z < y > x:
        print(f"{y} is the biggest")

    elif z == y == x:
        print("all three numbers are equal")

    elif z==y<x:
        print(f"{x} is the biggest")
    elif z==y>x:
        print(f"{y} is the biggest")

    elif z == x < y:
        print(f"{y} is the biggest")
    elif z == x > y:
        print(f"{x} is the biggest")

    elif x == y < z:
        print(f"{z} is the biggest")
    elif x == y > z:
        print(f"{y} is the biggest")

highest_number(x,y,z)