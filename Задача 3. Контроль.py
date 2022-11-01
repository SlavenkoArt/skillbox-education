def employees(emp):
    id_employees = []
    for _ in range(emp):
        id = int(input('ID сотрудника: '))
        id_employees.append(id)
    return id_employees

def counter(id_employees, search_id):
    counter = 0
    for symbol in id_employees:
        if symbol == search_id:
            print('Сотрудник на месте.')
        elif symbol != search_id:
            counter += 1
    return counter

emp = int(input('Количество сотрудников в офисе: '))

emp_count = employees(emp)

search_id = int(input('Какой ID ищем: '))

counter = counter(emp_count, search_id)

if counter == emp:
    print('Сотрудник не работает!')