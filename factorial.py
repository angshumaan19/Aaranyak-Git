def factorial(x):
    """this is a recursive function to find
     factorial of an integer"""

    if x== 1 or x==0:
        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__,"\n \n")
print("the factorial of 0 is",factorial(0),"\n")
print("the factorial of 1 is",factorial(1),"\n")
print("the factorial of 2 is",factorial(2),"\n")
print("the factorial of 3 is",factorial(3),"\n")
print("the factorial of 5 is",factorial(5),"\n")
print("the factorial of 10 is",factorial(10),"\n")
print("the factorial of 50 is",factorial(50),"\n")
print("the factorial of 100 is",factorial(100),"\n")
