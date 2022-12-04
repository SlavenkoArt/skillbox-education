participants = int(input('Количество участников: '))
team = int(input('Количество человек в команде: '))
num = 1
num_list = []

if participants % team != 0:
    print(participants, 'участников невозможно поделить на команды по', team, 'человек.')
else:
    for _ in range(participants // team):
        num_list.append(list(range(num, num + team)))
        num += team
    print(num_list)