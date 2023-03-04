speakers_file = open('/Users/artemslavenko/Desktop/group_1.txt', 'r', encoding='utf-8')
data = speakers_file.read()
speakers_file2 = open('/Users/artemslavenko/Desktop/skillbox-education/group_2.txt',
                      'r', encoding='utf-8')
data2 = speakers_file2.read()
summa = 0
diff = 0
compose = 1

for sym in data.split():
    if sym.isdigit():
        summa += int(sym)
        diff -= int(sym)

print(summa)

print(diff)
speakers_file.close()

for sym in data2.split():
    if sym.isdigit():
        compose *= int(sym)

print(compose)
print(data)
print(data2)