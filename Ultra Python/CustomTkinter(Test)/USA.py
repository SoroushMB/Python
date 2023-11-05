"""The library for introducing USA states!"""
class California:
    def large():
        return "Los Angeles"
    def capital():
        return "Sacramento"
    def area():
        return 4.24e5
    def population():
        return 3.924e7

class New_York:
    def large():
        return "New York City"
    def capital():
        return "Albany"
    def area():
        return 1.413e5
    def population():
        return 1.984e7

class Florida:
    def large():
        return "Jacksonville"
    def capital():
        return "Tallahassee"
    def area():
        return 1.703e5
    def population():
        return 2.178e7

if __name__ == "__main__":
    city1 = California()
    city2 = New_York()
    city3 = Florida()

    for name in (city1,city2,city3):
        print(f"{name.large()}")