class Lasagna:
    def __init__(self,prep_time:int=20,bake_time:int=40) -> int:
        self.prep_time = prep_time
        self.bake_time = bake_time
    def total_prep_time(self):
        return self.prep_time + self.bake_time
food = Lasagna()
print(food.total_prep_time())