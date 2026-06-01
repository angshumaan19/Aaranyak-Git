#the marks
math = int(input("enter the marks"))
hindi = int(input("enter the marks"))
tamil = int(input("enter the marks"))
english = int(input("enter the marks"))
art = int(input("enter the marks"))
evs = int(input("enter the marks"))
comp_science = int(input("enter the marks"))

sum = math + hindi + tamil + english + art + evs + comp_science

print("the sum of marks is",sum)

perc = (sum/700)*100

print("the percentage of marks obtained is",perc,"%")