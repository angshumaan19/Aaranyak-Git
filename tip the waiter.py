def total_calculate(bill_amount,tip_percentage):
    total = bill_amount * (1 + 0.01 * tip_percentage)
    total = round(total,2)
    print(f"please pay ₹{total}")


total_calculate(1500,2)