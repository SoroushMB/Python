# Boolean , Tuple
# user_agreement = bool(input("Do you agree with our policy? ")) # True
# if user_agreement: # True = If we type something 
#     print("You agree to our policy!")
# else: # False = If we don't type anything!
#     print("You cannot continue to install our app!")
# names = ("Kooshan","Arshak","Arisa") # Tuple
# def squaring(number):
#     global name
#     name = "Soroush"
#     return number ** 2
# print(name)
# number = squaring(number=25)
# print(number)
names = ["Kooshan","Arshak","Arisa"] # List
another_names = ["Sina","Soroush"]
# names.pop(1)
names.extend(another_names)
names.reverse()
print(names)