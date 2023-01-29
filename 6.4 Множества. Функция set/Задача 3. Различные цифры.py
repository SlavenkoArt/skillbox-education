text = set(input('Введите строку: '))
numbers = '0123456789'
print(''.join(text.intersection(numbers)))

# text_unique = set(text)
# result = text_unique & set("0123456789")
# print(''.join(result))

# new_result = set()
# for symbol in text:
#     if '0' <= symbol <= '9':
#         new_result.add(symbol)
# print(''.join(new_result))