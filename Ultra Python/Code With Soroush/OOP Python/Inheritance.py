from USA import California

class Selected_City(California):
    def __init__(self):
        self.largest_city = California.large()

city = Selected_City()
print(city.largest_city)