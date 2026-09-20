import array as arr

basket1={'apple','banana','mango','orange','pineapple'}
basket2={'banana','apple','cherry','orange','blueberry'}

print(f"basket 1:{basket1},basket 2:{basket2}")
common_fruits=basket1.intersection(basket2)


fruit_counts = arr.array('i',[1,2,3,4,5,6,7])

print("")

print("===== CLASS FRUIT BASKET ORGANIZER =====")

print("Basket 1:", basket1)

print("Basket 2:", basket2)

print("Shared fruits:", common_fruits)

print("Fruit counts:", fruit_counts)

print("===========================================")
print("")
