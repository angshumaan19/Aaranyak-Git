habit_info = ("playing",True,7,20.5)
print(habit_info)

weekly_habit_tracker=(1,0,0,1,1,1,0)
print(weekly_habit_tracker)

print("number of days :",len(weekly_habit_tracker))

print("first day habit :",weekly_habit_tracker[0])
print("third day habit :",weekly_habit_tracker[2])

print("first four weekday habits :",weekly_habit_tracker[0:4])
print("weekend habits :",weekly_habit_tracker[5:7])

weekly_habit_tracker = weekly_habit_tracker + (1,)
print(weekly_habit_tracker)

print("completed days :",weekly_habit_tracker.count(1))
print("missed days :",weekly_habit_tracker.count(0))

