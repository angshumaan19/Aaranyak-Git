import array as a
snack_box1 = {'chips','bananas','cold drinks','apples','bananas','grapes'}
snack_box2 = {'bread','burgers','cheese','sandwich','bread','apples','grapes'}
print(snack_box1)
print(snack_box2)
snack_box1.add('chocolate')
print(snack_box1)
print(snack_box1.intersection(snack_box2))

array1 = a.array('i',[1,3,3,2,5,5,9,2])
array1.insert(5,2)
print(array1)
array1.append(10)
print(array1)
print(array1.count(3))
array1.reverse()
print(array1)

print("")
print("===FINAL SUMMARY===")
print("snack box 1 :",snack_box1)
print("snack box 2 :",snack_box2)
print("common snacks in both snack boxes :",snack_box1.intersection(snack_box2))
print("both snack box in 1 set :",snack_box1.union(snack_box2))
print("array1 :",array1)
print("reverse of array1 :",array1)