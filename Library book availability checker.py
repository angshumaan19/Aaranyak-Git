books = ["wimpy kid", "harry potter", "wonder", "the jungle book", "dog man"]
copy_counts = [4, 0, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library Stock:", library)

available_books = [book for book in books if library[book] > 0]
print(f"books available : {available_books}\n")

chosen_book = input("Which book do you want to borrow? ")
if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "is not available! Stopping the checker.")
    exit()

late_fees= [5,8,4,6,7]
extra_fees =int(input("Enter the extra library fee to add every book: "))

updated_fees = list(map(lambda fee:fee + extra_fees , late_fees))
print("updated late fees :",updated_fees)

book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]
print("late fee for",chosen_book,"after_fee",chosen_fee)

library[chosen_book] = library[chosen_book] - 1
print(chosen_book, "borrowed! Remaining copies:", library[chosen_book])

print("")
print("===== LIBRARY BOOK AVAILABILITY CHECKER =====")
print("books_borrowed =",chosen_book)
print("late fee =",chosen_fee)
print("updated library stock =",library)