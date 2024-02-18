from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cash_data = OrderedDict()
        self.order = []

    @property
    def cache(self):
        return self.cash_data

    @cache.setter
    def cache(self, new_elem):
        if len(self.cash_data) < self.capacity:
            self.cash_data[new_elem[0]] = new_elem[1]
            self.order.append(new_elem[0])
        else:
            self.cash_data.pop(self.order[0])
            self.order.pop(0)
            self.cash = new_elem

    def get(self, key):
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
        return self.cash_data.get(key)

    def print_cache(self):
        print('LRU Cache:')
        for key in self.order:
            print('    {}:{}'.format(key, self.cash_data[key]))

    # Создаем экземпляр класса LRU Cache с capacity = 3


cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
