secret=45
x=0
tries=5


while tries != x:
    tries-=1
    num = int(input("guess the number"))
    difference = abs(secret - num)
    if num == secret:
        print("the secret is revealed :",secret)
        break
    if difference > 40:
        print("ice cold")
    elif difference > 30:
        print("cold")
    elif difference > 20:
        print("warm")
    else:
        print("hot")

    if tries > 0:
        print(f"attempts = {tries}")
        print(f"hearts = {"❤️"*tries}")

else:
    print("you lost the number was",secret)
