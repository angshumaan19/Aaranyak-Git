# STEP 1:define a function
def greet_customer():
    print("welcome to the lemonade stand")
    print("fresh lemonade for you")

# STEP 2:call the function
greet_customer()

# STEP 3:ask the user to enter the price per cup and cups
price_per_cup=float(input("enter the price per cup"))
cups=int(input("enter the number of cups"))

# STEP 4:define a function that takes argument and returns the total cost
def calculate_total(price,cup):
    p = price * cup
    return p

# STEP 5:call the 'calculate total' and you are going to store the value in returns
total_cost = calculate_total(price_per_cup,cups)

# STEP 6:round off the total cost
rounded_total=round(total_cost,2)

print("the total cost:",rounded_total)
# STEP 7:ask the customer how much he/she paid

amount=float(input("enter the money you paid"))
# STEP 8:define calculate change and return the change due
def calculate_change(paid,total):
    change = paid - total
    return change

# STEP 9:call calculate change and store the value it returns
change_due=calculate_change(amount,rounded_total)
rounded_change = round(change_due,2)

# STEP 10:define a thankyou message for the number of cups sold
def thankyou(cups):
    if cups >= 5:
        return "wow that's a huge order,we thank ypu for your support"
    else:
        return "thank you for stopping by"

# STEP 11:call thankyou message and store the value it returns
thank = thankyou(cups)

# STEP 12:print the receipt
print("====LEMONADE STAND RECEIPT====")
print("price per cup  :",price_per_cup)
print("total cups sold:",total_cost)
print("total cost     :",rounded_total)
print("amount paid    :",amount)
print("change due     :",change_due)
print(thank)
print("===============================")

