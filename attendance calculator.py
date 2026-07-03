medical_cause=input("did you have a medical cause(Y/N)").strip().upper()
if medical_cause == "Y":
    print("you are allowed")
elif medical_cause == "N":
    attendance=int(input("enter your attendance(numbers only)"))
    if attendance >= 75:
        print("you are allowed")
    else:
        print("you are not allowed")
else:
    print("invalid input")