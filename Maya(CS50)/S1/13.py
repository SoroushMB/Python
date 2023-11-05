name = input("What's your name? ")

match name:
    case "Iron Man" | "War Machine":
        print("Tech")
    case "Thor" | "Captain Marvel":
        print("Lightning")
    case "Hulk":
        print("Super bi asab!")
    case other:
        print("Who?")
# Switch Case