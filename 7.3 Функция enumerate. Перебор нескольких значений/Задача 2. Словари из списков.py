first_list = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
second_list = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

first_list_dict = {}
second_list_dict = {}

for index, sym in enumerate(first_list):
    first_list_dict[index] = sym

for index, sym in enumerate(second_list):
    second_list_dict[index] = sym

print(first_list_dict)
print(second_list_dict)