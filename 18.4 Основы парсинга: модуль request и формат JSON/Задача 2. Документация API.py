import json

import requests

# file = requests.get('https://swapi.dev/api/')
# print(file.text)
# json_file = json.loads(file.text)
# print(json_file['films'])
# new_file = requests.get(json_file['films'])
# print(new_file.text)

result = requests.get("https://swapi.dev/api/films/2/")

json_dict = json.loads(result.text)
print(json_dict)

print(json_dict["opening_crawl"])
