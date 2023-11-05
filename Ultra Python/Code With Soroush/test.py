name = input(">> ")
# if name == "Arian":
#     print("Hi")
# elif name == "Mani":
#     print("Very High!")
# elif name == "Sourena":
#     print("So many problems!")
# else:
#     print("Who?")
match name:
    case "Arian":
        print("Hi")
    case "Mani":
        print("Very High!")
    case "Sourena":
        print("So many problems!")
    case other:
        print("Who?")