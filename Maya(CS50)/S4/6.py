import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

javab = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(javab.json(), indent=2))