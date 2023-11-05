# sourcery skip: remove-redundant-continue, remove-unnecessary-else, swap-if-else-branches
# 21, January 1378 -> 1378-01-21
months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}
while True:
    user_date = input("Date:")
    if " " in user_date:
        month, day, year = user_date.split(" ")
        month = month.capitalize()
        day = day.replace(',','')
        if day.isdigit():
            day = int(day)
            if day <= 31:
                print(f"{year}-{months[month]}-{day:02}")
                break
            else:
                continue
        else:
            continue
    elif "/" in user_date:
        month, day, year = user_date.split("/")
        day, month = int(day), int(month)
        if day <= 31 and month <= 12:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue