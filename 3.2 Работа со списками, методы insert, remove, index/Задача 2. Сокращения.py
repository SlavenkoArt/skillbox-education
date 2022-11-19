salary_list = []

employee = int(input('Количество сотрудников: '))

for i in range(employee):
    print('Зарплата', i + 1, 'сотрудника: ')
    salary = int(input(''))
    salary_list.append(salary)

for i in salary_list:
    if i == 0:
        salary_list.remove(i)

print('Осталось сотрудников: ', len(salary_list))
print('Зарплаты: ', salary_list)

print('Максимальная зп: ', min(salary_list))
print('Минимальная зп: ',max(salary_list))