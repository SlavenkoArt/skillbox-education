class CountIteretor():
    def __init__(self):
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1
        return self.__count


my_iter = CountIteretor()

for i_elem in my_iter:
    print(i_elem)