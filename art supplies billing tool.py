# STEP:1
def greet():
    print("welcome to the art supplies shop!")
    print("get your colors,paint and oil pastels here!\n")
# STEP:2
greet()
# STEP:3
price_per_item=float(input("enter the price per item"))
items_bought=int(input("enter how many items you want"))
# STEP:4
def calculate_total(price, items):
    total = price * items
    return total
# STEP:5
total_items=calculate_total(price_per_item,items_bought)
# STEP:6
rounded_items=round(total_items,2)
print("total items =",rounded_items)
# STEP:7
amount=float(input("how many items did you buy"))
# STEP:8
def calculate_change(paid,total):
    t = paid - total
    return t
# STEP:9
def thankyou(items):
    if items >= 5:
        return "wow, what a huge order .Thank you for the support"
    else:
        return "thank you for coming here"

thank = thankyou(items_bought)

print("====ART SUPPLIES RECEIPT====")
print("price per item    :",price_per_item)
print("items bought      :",items_bought)
print("total items       :",rounded_items)
print("amount            :",amount)
print(thank)
print("==============================")








