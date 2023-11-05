user_time = input("What time is it? ")# 7:35

hours,minutes = user_time.split(":")
result = int(hours) + (int(minutes)/60)

match result:
    case 7:
        print("Breakfast Time!")
    case other:
        print()