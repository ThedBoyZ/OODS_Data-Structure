class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None
    
    def __repr__(self):
        return f'{self.val}'


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.header
        self.header.next = self.tail
        self.size = 0

    def __repr__(self):
        return str(self.get_item())

    def __getitem__(self, item):
        index = 0
        current_node = self.header.next
        while current_node:
            if index == item:
                return current_node
            current_node = current_node.next
            index += 1
        return None
    
    def add_right(self, val):
        node = Node(val)
        last_node = self.tail.prev
        last_node.next = node     
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node    
        self.size += 1

    def add_left(self, val):
        node = Node(val)
        first_node = self.header.next
        self.header.next = node     
        node.prev = self.header
        node.next = first_node
        self.tail.prev = node    
        self.size += 1

    def del_head(self):
        if self.size == 0:
            return 0
        self.head.next = self.head.next.next
        self.size -= 1
        return 1

    def del_tail(self):
        if self.size == 0:
            return 0
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return 1

    def is_empty(self):
        return self.size == 0

    def search(self, keyword):
        index = 0
        current_node = self.head.next
        while current_node:
            if current_node.val == keyword:
                return index
            index += 1
            current_node = current_node.next
        return -1

    def insert(self, pos, val):
        if not(0 <= pos <= self.size):
            return 0
        if pos == 0:
            self.add_left(val)
            return 1
        if pos == self.size:
            self.add_right(val)
            return 1
        index = 0
        current_node = self.head.next
        node = None(val)
        while current_node:
            if index == pos:
                prev_node = current_node.prev
                prev_node.next = node
                node.prev = prev_node
                node.next = current_node
                current_node.prev = node
                self.size += 1
                break
            current_node = current_node.next
            index += 1
        return 1

    def get_item(self):
        res = []
        current_node = self.head.next
        while current_node:
            if current_node.val is not None:
                res.append(str(current_node.val))
            current_node = current_node.next

        return res

class DoublyLinkedList_OOD_Given(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def __reverse(self):
        res = []
        last_node = self.tail.prev
        while last_node:
            if last_node.val is not None:
                res.append(str(last_node.val))
            last_node = last_node.prev
        return res
    
    def str_reversed(self):
        return "->".join(self.__reverse())
    
    def remove(self, keyword):
        index = 0
        current_node = self.header.next
        while current_node:
            if current_node.val == keyword:
                prev_node = current_node.prev
                next_node = current_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                self.size -= 1
                return current_node, index
            current_node = current_node.next
            index += 1
        return None, None


    L = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        elif i[:2] == "SI":
            print("Linked List size = {0} : {1}".format(L.size(), L))
        elif i[:2] == "ID":
            print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
        elif i[:2] == "PO":
            before = "{}".format(L)
            k = L.pop(int(i[3:]))
            print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
        elif i[:2] == "IS":
            data = i[3:].split()
            L.insert(int(data[0]), data[1])

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())