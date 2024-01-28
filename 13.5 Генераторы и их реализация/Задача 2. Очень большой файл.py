def numbers_of_text(text):
    return [int(number) for number in text.rstrip().split()]
def count(file):
    with open(file) as sym:
        for i in sym:
            sym_line = sum(numbers_of_text(i))
            yield sym_line


all_summ = 0

for num in count("numbers.txt"):
    all_summ += num

print('Вариант 1', all_summ)



def count(file):
    with open(file) as sym:
        for i in sym:
            sym_line = sum(map(int, i.rstrip().split()))
            yield sym_line


all_summ = 0

for num in count("numbers.txt"):
    all_summ += num

print('Вариант 2', all_summ)