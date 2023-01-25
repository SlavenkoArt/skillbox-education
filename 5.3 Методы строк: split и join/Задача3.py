
while True:
    text = input('Введите шаблон поздравления. В шаблоне можно исполбьзовать конструкцию {name} и {age}: ')
    if '{name}' in text and '{age}' in text:
        break
    print('Отсутствует одна или несколько конструкций!')

people = input('Список людей, через запятую: ').split(',')
ages_str = input('Введите возраст, через пробел: ')
ages = [int(age) for age in ages_str.split()]

for index, name in enumerate(people):
    print(text.format(name=name, age=ages[index]))

for age, name in zip(ages, text):
    print(text.format(name=name, age=age))

people = [" ".join([people[index], str(ages[index])]) for index in range(len(people))]
print("Именинники:", ", ".join(people))