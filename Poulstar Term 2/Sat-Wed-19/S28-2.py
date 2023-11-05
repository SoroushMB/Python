# String Methods : Capitalize , Title , Lower , Upper , Remove(Replace) , isdigit

phonenumber = input(">> ")
validation = phonenumber.isdigit()
length_of_string = len(phonenumber)

if validation == True and length_of_string <= 11:
    print("Your phone number format is correct")
elif validation == True and length_of_string > 11:
    print("Your phone number format is correct but your length of characters isn't what we wanted!")
else:
    print("You are daghan!")