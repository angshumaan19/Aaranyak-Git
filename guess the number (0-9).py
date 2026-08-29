import random as rand
playing = True
number = str(rand.randint(0,9))
while playing:
    player = str(input("enter a number(0-9)"))
    if player== number:
        print("you got the number!")
        print("the number was",number)
        playing = False
    else:
        print("you lose,dont worry try again")