# names.extend(others)
# for name in names:
#     print(name)
# names.append("Barbod")
# names.remove("Taha")
#
# names.pop(0)
# names.clear()
# user_selected = input("Which name do you want to delete? ")
# names.remove(user_selected)
# names = ("Parmida","Reyhaneh","Barbod")
names = ["Taha","Yalda"]
others = ["Soroush","Mohammed Ali","Sepideh"]
others.reverse()
for name in others:
    names.insert(0,name)
print(sorted(names))
print(len(names))
