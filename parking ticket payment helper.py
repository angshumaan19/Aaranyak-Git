def calculate_change(paid,price):
    change = paid - price
    return change

ticket_price=30

print("=== PARKING TICKET PAYMENT HELPER ===")
print("the ticket price is",ticket_price)
print("the accepted coins are 1,2,5,10,25")

total_inserted=0
coins_inserted=0

s = True

while s:

    coin=int(input("enter a coin {1,2,5,10,25}"))
    if coin != 1 and coin != 2 and coin != 5 and coin != 10 and coin != 25:
        print("invalid input.Please try again")
        continue
    total_inserted += coin
    coins_inserted += 1


    print("total payed :",total_inserted)

    if total_inserted >= ticket_price:
        print("stop paying any more coins.it is enough for payment")
        s = False



change_due = calculate_change(total_inserted,ticket_price)

if change_due == 0:
    pass
else:
    print(change_due)

print(">>> PAYMENT TICKET <<<")
print("ticket price  :",ticket_price)
print("coins inserted:",coins_inserted)
print("total inserted:",total_inserted)
print("change given  :",change_due)