# PART:1
list1=[]
print(list1)
marks = [100,100,100,99.5,99]
print("marks :",marks)

# PART:2
sample_marks = [10,20,30] * 2
print(f"Repeated sample marks : {sample_marks}")

# PART:3
print(len(marks))

# PART:4
print(f"first marks : {marks[0]},last marks : {marks[-1]}")

# PART:5
print(f"first 3 marks : {marks[0:2]}")
print(f"reversed marks : {marks[::-1]}")

# PART:6

def match(mark_list):
    count=0
    matched_marks = []

    for mark in mark_list:
        mark_text = str(mark)
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks = mark.append()

        print("marks with first and last value same:",matched_marks)
        return count
    return None

same_digit_count=match([67 , 87 , 45 , 59 , 60])
print("number of matching marks:",same_digit_count)

# PART:7

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("sum of marks:",total)
print("average marks:",average)

marks.sort()

print("smallest marks =",marks[0])
print("largest marks =",marks[-1])


print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])
print("=======================================")
