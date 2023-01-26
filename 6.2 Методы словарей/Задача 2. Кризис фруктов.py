
total_sum = 0

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

result_sum = 0
min_value = None
min_name = ""
for name, value in incomes.items():
    result_sum += value
    if min_value is None or min_value > value:
        min_value = value
        min_name = name

incomes.pop(min_name)

print(f"Общий доход за год составил {result_sum} рублей")
print(f"Самый маленький доход у {min_name}. Он составляет {min_value} рублей")
print("Итоговый словарь:", incomes)