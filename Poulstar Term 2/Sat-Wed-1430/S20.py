info = []
try:
    user_name = str(input("Name : "))
    user_phonenumber = str(input("Phonenumber : "))
    user_age = int(input("Age : "))
    user_maritalstatus = str(input("Marital status : "))
    user_height = float(input("Height : "))
    
    info.append(user_name)
    info.append(user_phonenumber)
    info.append(user_age)
    info.append(user_maritalstatus)
    info.append(user_height)
    
    print(f"Username : {info[0]}\nPhone number : {info[1]}\nAge : {info[2]} \nMarital status : {info[3]}\nHeight : {info[4]}\n")
except ValueError:
    print("You have entered a wrong value!")
    
# File Handling in Python