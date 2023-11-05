Name = input(">> ")

# if Name == "Soroush" or Name == "Kourosh":
#     print("BlahBlahBlahBlah!!!")
# else:
#     print("AnotherBlah!")
# 
match Name:
    case "Soroush" | "Kourosh":
        print("BlahBlahBlahBlah!!!")
    case other:
        print("AnotherBlah!")