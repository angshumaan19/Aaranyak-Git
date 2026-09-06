import random
password=random.randint(1000,9999)
keys = 0
tries = 5

while keys < tries:
    num = int(input("guess the number"))
    difference = abs(password - num)
    tries -= 1

    if num == password:
        print("✅ you got it",password,"!")
        break
    if difference > 5000:
        print("❤️ very far")
    elif difference > 2000:
        print("🧡 far")
    elif difference > 500:
        print("💛 close")
    else:
        print("💚 very close")

    if tries > 0:
        print(f"keys = {"🔑" * tries}")
        print(f"tries = {tries}")



if tries == keys:
    print("you're out, the answer is",password)



