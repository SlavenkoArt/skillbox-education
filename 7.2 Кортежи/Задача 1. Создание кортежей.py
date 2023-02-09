import random

first_tuple = tuple(random.randint(0, 5) for _ in range(10))
print(first_tuple)

second_tuple = tuple(random.randint(-5, 0) for _ in range(10))
print(second_tuple)

third_tuple = first_tuple + second_tuple
print(third_tuple)
print(third_tuple.count(0))