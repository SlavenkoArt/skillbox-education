def endless_count(number=0):
    while True:
        number += 1
        yield number

num = endless_count()
for i in num:
    print(i)