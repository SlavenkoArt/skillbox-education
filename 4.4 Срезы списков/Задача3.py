import random

N = 100
A = random.randint(0, 100)
B = random.randint(A, 100)

new_list = [i for i in range(N + 1)]

new_list[A:B + 1] = []
print(new_list)