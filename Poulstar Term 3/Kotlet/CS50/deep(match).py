Annanaz = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace("_","").replace("-","").replace(" ","").lower()

match Annanaz:
    case "fortytwo" | "42":
        print("Yes")
    case other:
        print("No")