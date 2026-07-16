print("ATM cash dispenser")
print("dispensing cash to customers\n")
# initialize variables
notes = [100,50,20,10,5,2,1]
# list on available notes

customer_served=0
# customers who have used the ATM

total_dispensed=0
# the amount withdrawn

log=[]
# store each customer's note details

# outer while loop
serving = True
while serving:
    name = str(input("enter your name:"))
    amount = int(input(f"hello {name}! enter the amount you want to withdraw"))
    if amount <= 0:
        print("invalid input please try again")
        continue
    print(f"\nthe dispersing cash is {amount} for {name}")
    print("-" * 30)

    remaining = amount
    i = 0
    used = {}
    # inner while loop - breaking amount into rupees
    while i<(len(notes)):
        count = remaining // notes[i]
        if count > 0:
            print(f"{count} x {notes[i]} - unit notes = {count * notes[i]}")
            used[notes[i]] = count
            remaining -= count * notes[i]
        i += 1
    customer_served += 1
    total_dispensed += amount
    log.append({'name':name,"used":used})
    print(f"transaction complete! please collect your cash {name}")

    again = str(input("next customer (yes/no) ?")).strip().lower()
    if again != "yes":
        serving = False
print("\n---Daily Denomination Report---")
for note in notes:
    total_notes = 0
    for entry in log:
        total_notes += entry["used"].get (note,0)

    if total_notes > 0:
        print(f"{note}-total notes dispersed today : {total_notes}")

print(f"total customers served : {customer_served}")
print(f"total amount dispersed : {total_dispensed}")
print("ATM is closed. bye!")



