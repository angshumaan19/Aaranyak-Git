num=int(input("enter a number"))
pow=int(input("enter the power"))
res=1

for i in range(pow):
    res *= num
print(num,"to the power of",pow,"is",res)