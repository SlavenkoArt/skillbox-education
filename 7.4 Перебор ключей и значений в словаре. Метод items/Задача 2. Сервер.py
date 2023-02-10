server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for sym, i_data in server_data.items():
    print(f'{sym} :')
    for i_key, i_meaning in i_data.items():
        print(f'\t{i_key} : {i_meaning}')
