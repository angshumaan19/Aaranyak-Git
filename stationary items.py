items = ['pencil','eraser','notebook','sharpener','glue']
stock_counts = [12,0,8,5,3]
inventory = {item: count for item,count in zip(items,stock_counts)}
print('full inventory :',inventory)
in_stock_items = [item for item in items if inventory[item] > 0]
chosen_item = input('which item you want to buy?')
if chosen_item not in items or inventory[chosen_item] == 0:
    print(chosen_item,"is out of stock,stop the checker" )
    exit()

price = [10,5,15,30,40]
markup = int(input("enter the the markup price"))

markup_prices = list(map(lambda p:p + markup,price))
print(markup_prices)

item_index = items.index(chosen_item)
chosen_price = markup_prices[item_index]

print("price of",chosen_item,"is",chosen_price)

inventory[chosen_item] = inventory[chosen_item]-1
print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])

print("")

print("===== SCHOOL STORE INVENTORY CHECKER =====")

print("Item Bought:", chosen_item)

print("Price Paid:", chosen_price)

print("Updated Inventory:", inventory)

print("=============================================")

