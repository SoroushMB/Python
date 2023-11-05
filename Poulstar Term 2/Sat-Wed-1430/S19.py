name = "Anisa"
other_name = "Mehrab"
# other_names = ("Sadra","Anahid","Arian","Makan","Ilya","Parsa","Sam","Anisa","Mehrab") # tuple
names = ["Sadra","Anahid","Arian","Makan","Ilya","Parsa","Sam","Anisa","Mehrab","Reza"] # list
user_input = input("Name : ")
names.append(user_input)
other_user_input = input("The name you want to delete : ")
names.remove(name)
counter = len(names)
print(names)
print(counter)
print(names.index("Reza"))