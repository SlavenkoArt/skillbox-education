import json
import requests

file = requests.get('https://swapi.dev/api/people/3/')

if file.status_code == 200:
    json_file = json.loads(file.text) #десириализация JSON
    json_file['name'] = input('Введите ваше имя: ')
    with open('my_file.json', 'w') as file:
        json.dump(json_file, file, indent=4) #сериализация JSON

    new_file = requests.get(json_file['homeworld'])
    print(new_file.text)

with open('my_file.json', 'r') as file:
    data = json.load(file)

