

print("===GROCERY BILLING QUEUE===")
print("billing grocery for customers\n")
low_price=0
medium_price=0
high_price=0

customers_sold=0
total_sales=0

billing = True
while billing:
    name=str(input("what is the customer's name"))
    grocery_items=int(input(f"enter the number of grocery items for {name}"))

    if grocery_items <= 0:
        print("invalid input, please enter a positive number.")
        continue

    print("\nbilling items for customers")
    customer_number=0
    item_num = 1

    while item_num >= grocery_items:
        item_name=str(input("what is the item name"))
        price=int(input("what is the price of the item"))
        quantity=int(input("what is the quantity of the item"))

        if price <= 0 or quantity <= 0:
            print("invalid price or quantity.please entera positive number")
            continue

        item_total=price * quantity
        print(f"{item_name} : {price} x {quantity} = {item_total}")
        customers_sold += item_total

        if price < 50:
             low_price += quantity
        elif price <= 100:
            medium_price += quantity
        else:
            high_price += quantity

        item_num += 1

    customers_sold += 1

    total_sales += customer_number

    print(f"\ntotal bill for {name} : {customer_number}")
    print("billing complete")

    c=str(input("another customer? (yes/no)")).strip().lower()
    if c != "yes":
        billing = False


print("===FINAL GROCERY REPORT===")

for slot in range(1,4):
    if slot == 1:
        label,total="low value items",low_price
    elif slot == 2:
        label,total="medium value items",medium_price
    else:
        label,total="high value items",high_price

    if total > 0:
        print(f"{label}:{total}",end="")
        for item in range(total):
            print("*",end="")


    print()

print(f"customers served : {customers_sold}")
print(f"total sales : {total_sales}")

print("grocery billing closed.Goodbye!")


