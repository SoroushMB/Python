# randint , randrange , choice , shuffle
from random import shuffle,choice

names = ["Saman","Avesta","Younes","Mani","Aran"]
shuffle(names)
chosen = choice(names)
print(chosen)