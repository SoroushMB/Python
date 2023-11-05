def main():
    user_time = input("What time is it? ")
    converted = convert(time=user_time)
    if 8 <= converted <= 9:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")

def convert(time):
    hour,min = time.split(":")
    hour,min = int(hour),int(min)/60
    return hour+min

if __name__ == "__main__":
    main()