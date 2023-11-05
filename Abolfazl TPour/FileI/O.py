# File I/O -> Write(Input) , Read(Output)
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
    userDate = input("Date:")
    if " " in userDate:
        month, day, year = userDate.split(" ")
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
    elif "/" in userDate:
        month, day, year = userDate.split("/")
        day, month = int(day), int(month)
        if day <= 31 and month <= 12:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue