site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search = input('Искомый ключ: ')

def find_key(stuct, key):
    if key in stuct:
        return stuct[key]

    for sym in stuct.values():
        if isinstance(sym, dict):
            result = find_key(sym, key)
            if result:
                break
    else:
        result = None

    return result

print(find_key(site, search))