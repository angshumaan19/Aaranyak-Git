student_data = {
"id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
"id2": {"name": "David", "class": "V", "subject": "english, math, science"},
"id3": {"name": "Saran", "class": "V", "subject": "english, math, science"},
"id4": {"name": "Surya", "class": "V", "subject": "english, math, science"},
}

print("the original student data:",student_data)

print(student_data.get('id1','not found'))

print(student_data.get('id5','not found'))

student_data['id5'] = {"name": "Ananya",
                       "class":"V",
                       "subject": "english, math, science"}

print("")
print("after adding id5:")
print(student_data)

student_data['id2']['subject'] = "english, math, coding"

print("")
print("after updating id2 subject:")
print(student_data)

cleaned_data = {}
seen_records = []

for student_id,details in student_data.items():
    unique_data=(details['name'],details['class'],details['subject'])

    if unique_data not in seen_records:
        seen_records.append(unique_data)
        cleaned_data[student_id] = details

student_data = cleaned_data

removed_student = (student_data.pop("id4","student not found"))

print("")
print("removed student")
print(removed_student)

print("the length of the of the final dictionary:")
print(len(student_data))

print("===FINAL STUDENT SUBJECT RECORD===")

for student_id, details in cleaned_data.items():
    print(student_id, ':', details)