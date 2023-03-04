numbers = open('speakers.txt', 'r', encoding='utf-8')
count = 0

for num in numbers:
    count += int(num)

numbers.close()

counts_file = open('answer.txt', 'w')
counts_file.write(str(count))
counts_file.close()
