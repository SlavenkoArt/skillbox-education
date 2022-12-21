import random

first_list = [random.randint(50, 80) for _ in range(10)]
second_list = [random.randint(30, 60) for _ in range(10)]

third_list = [('Погиб' if first_list[i] + second_list[i] > 100 else 'Выжил')
              for i in range(10)]

print('Урон первого отряда', first_list)
print('Урон второго отряда ', second_list)
print('Состояние третьего отряда ', third_list)
