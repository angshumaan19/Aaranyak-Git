def total_bill(bill_amount,tip_perc):
    total = bill_amount * (0.01 + 1 * tip_perc)
    total = round(total,2)
    print(f"please pay ₹{total}")
    return total
total_bill(150,20)
def seating_arrangements(guests):
    """this is a recursive case to find the number of
     seating arrangements for guests"""


    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * seating_arrangements(guests - 1)


print(seating_arrangements.__doc__)

print("seating arrangements for 1 guest",seating_arrangements(1))
print("seating arrangements for 2 guests",seating_arrangements(2))
print("seating arrangements for 3 guests",seating_arrangements(3))
print("seating arrangements for 5 guests",seating_arrangements(5))
print("seating arrangements for 10 guests",seating_arrangements(10))