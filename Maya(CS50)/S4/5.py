import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

javab = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

with open("test.json","a") as file:
    file.write(str(javab.json()))