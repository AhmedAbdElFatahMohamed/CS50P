import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
# print(json.dumps(response.json(), indent=2))

O=response.json()

for result in O["results"]:
    print(result["trackName"])