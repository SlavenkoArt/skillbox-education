main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]
error = 0

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

for i in main:
    if i == 0:
        error += 1

print('Общий список задач: ',main)
print('Количество невыполненных задач: ', error)