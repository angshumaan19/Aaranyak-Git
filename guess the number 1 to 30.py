import random
magic_box=random.randint(1,30)
i=0
gems=4
while gems > i:
    gems -= 1
    guess=int(input("guess the number(1 to 30)"))
    difference = abs(guess - magic_box)
    if guess == magic_box:
        print("✅ correct!")
        break
    elif difference > 25:
        print("🔥 very hot")
    elif difference > 20:
        print("🌤️ warm")
    elif difference > 10:
        print("🌬️ chilly")
    else:
        print("❄️ freezing")

    if gems > 0:
        print("remaining gems = ", "💎" * gems)


if gems == i:
    print("you lost the ans was",magic_box)

if gems > 0:
    print("remaining gems =","💎" * gems)
    print("attempts =",gems)