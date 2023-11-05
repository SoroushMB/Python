# 7:00-8:00 -> Breakfast Time, 12:00-13:00 -> Lunch Time, 18:00-19:00 -> Dinner Time
user_time = input("What time is it? ")# 7:35

hours,minutes = user_time.split(":")
result = int(hours) + (int(minutes)/60)

if 7 <= result <= 8:
    print("Breakfast Time")
elif 12 <= result <= 13:
    print("Lunch Time")
elif 18 <= result <= 19:
    print("Dinner Time")
else:
    print()
