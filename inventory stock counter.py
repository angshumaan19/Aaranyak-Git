print("inventory stock counter")
print("counting stock for products one at a time")
box_sizes=[50,20,10,5,1]
products_counted=0
total_items=0
log = []

counting=True
while counting:
    product_name=str(input("enter the product_name"))
    quantity=int(input(f"enter the quantity for {product_name}"))

    if quantity <= 0:
        print("invalid quantity.please enter the quantity again")
        continue
    print(f"packing {quantity} for {product_name}")
    print("-" * 30)

    remaining=quantity
    i=0
    used={}

    while i < len(box_sizes):
        count = remaining // box_sizes[i]
        if count > 0:
            print(f"{count} x {box_sizes[i]} - unit notes = {count * box_sizes[i]}")
            used[box_sizes[i]] = count
            remaining -= count * box_sizes[i]
        i += 1

    products_counted += 1
    total_items += quantity
    log.append({"product_name":product_name,"used":used})

    print(f"stock counted successfully for {product_name}")

    again = str(input("is there any more items(yes/no)?")).strip().lower()
    if again != "yes":
        counting = False

print("=== Final box size report ===\n")

for box in box_sizes:
    total_boxes=0
    for entry in log:
        total_boxes += entry["used"].get (box,0)
    if total_boxes > 0:
        print(f"{box}-item boxes used today : {total_boxes}")

print(f"products counted : {products_counted}")
print(f"total items      : {total_items}")
print("inventory counting complete")






