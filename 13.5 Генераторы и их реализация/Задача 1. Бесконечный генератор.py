class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        pass



class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        pass

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        raise IndexError('Индекс отсутствует')

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        count = 0
        while current and count != index:
            prev = current
            current = current.next
            count += 1
        if current is None:
            raise IndexError('Индекс отсутствует')
        prev.next = current.next


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
