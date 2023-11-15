# JSON -> Java Script Object Notation => Dictionary(Python) <-> Object(JavaScript)
# .txt 👎 , .json 👍
# Python -> JSON (dump), JSON -> Python (load)
from json import dump,load

settings = {
    "bg" : "black",
    "fg" : "white"
}

with open("test.json","w") as file:
    dump(obj=settings,fp=file)

print("Finished!")
