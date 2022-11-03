number_of_points = [11, 17, 73, 80, 12]
maximum = number_of_points[1]
minimum = number_of_points[1]
vice_versa = []

for i in number_of_points:
    if maximum < i:
        maximum = i

    if minimum > i:
        minimum = i

for number in number_of_points:
    if maximum == number:
        number = minimum
    elif minimum == number:
        number = maximum
    vice_versa.append(number)
print(vice_versa)