def main():
    time = input("What time is it? ")
    result = convert(time)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")

def convert(time):
    hour,min = time.split(":")
    hour,min = int(hour),(int(min))/60
    return hour + min


main()