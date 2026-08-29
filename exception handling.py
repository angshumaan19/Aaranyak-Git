num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
try:
    result = num1/num2
    print(result)

except:
    print("invalid input.please try again")
finally:
    print("i will run whatever happens")