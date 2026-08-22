try:
   d1,d2 = eval(input("enter two numbers separating with comma like 20,2"))
   result = d1 / d2
   print(result)
except ZeroDivisionError:
    print("division by 0 is error!!")
except ValueError:
    print("enter the numbers by numbers not letters!!")
except SyntaxError:
    print("you need to put a comma between the numbers like 20,5")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("code ended")