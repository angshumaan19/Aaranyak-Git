print("right angle triangle pattern of (*):")
n=int(input("enter the number of rows you want"))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()