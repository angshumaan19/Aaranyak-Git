j=int(input("Enter the number of notes"))

note1=j//100
note2=(j%100)//50
note3=((j%100)%50)//10
note4=(((j%100)%50)%10)//1

print("the number of 100 notes are there in this number",note1)
print("the number of 50 notes are there in this number",note2)
print("the number of 10 notes are there in this number",note3)
print("the number of 1 notes are there in this number",note4)