
print("================================")
print("welcome to holiday planner")
print("================================")
print()

print("step one: which holiday")
print("1:beach holiday")
print("2:mountain holiday")

holiday=str(input("enter, 1 or 2?"))

if holiday == "1":
    print("step two:put your beach activity")
    print("1:swimming")
    print("2:sandcastle building")
    beach_holiday = str(input("1 or 2?"))
    if beach_holiday == "1":
        print("your pick: swimming")
        print("best time: morning")
        print("remember : carry sunscreen and water")
    elif beach_holiday == "2":
        print("your pick: sandcastle building")
        print("best time: evening")
        print("remember : carry bucket and spade")
    else:
        print("that is not a valid choice please enter 1 or 2 next play")
elif holiday == "2":
    print("step two:put your mountain activity")
    print("1:hiking")
    print("2:camping")
    mountain_holiday = str(input("1 or 2?"))
    if mountain_holiday == "1":
        print("your pick: hiking")
        print("best for : exploring trails")
        print("remember : wear comfortable shoes")
    elif mountain_holiday == "2":
        print("your pick: camping")
        print("best for : staying around nature")
        print("remember : carry a tent and flashlight")
    else:
        print("that is not a valid choice please enter 1 or 2 next play")

else:
    print("that is not a valid choice please enter 1 or 2 next play")


print("================================")
print("see you in your holidays!")
print("================================")
print()

