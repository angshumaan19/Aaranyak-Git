# Alphabet = str(input("enter an alphabet"))
# # if Alphabet not in ("A","B","c"):
# #     print("Not an Alphabet")
# # else:
# #     print(Alphabet, "is an Alphabet")


# Program to check if a character is an Alphabet using logical operators
# #AMethod 2 for cheking alphabets
# ch = input("Enter a character: ")
#
# # Check if character is between 'a' and 'z' OR between 'A' and 'Z'
# if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
#     print(f"{ch} is an Alphabet.")
# else:
#     print(f"{ch} is NOT an Alphabet.")

# Method 3 for checking alphabets

text = input("Enter a character: ")

for ch in text:
    if  ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        print(f"{ch} is an Alphabet.")
    else:
        print(f"{ch} is NOT an Alphabet.")
