info = input('Введите информацию через пробел\n'
             'имя, фамилия, город, место учебы, оценки: ')

list_info = dict()
student_info = info.split()

list_info['имя'] = student_info[0]
list_info['фамилия'] = student_info[1]
list_info['город'] = student_info[2]
list_info['место учебы'] = student_info[3]
list_info['оценки'] = []

for i_grade in student_info[4:]:
    list_info['оценки'].append(int(i_grade))

for key in list_info:
    print(key, '-', list_info[key])