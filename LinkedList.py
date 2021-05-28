class Node:
    def __init__ (self,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self , *elems):
        self.head = None
        for elem in elems[0]:
            self.push(elem)

    def __repr__(self):
        current = self.head
        str = '[ '
        while current is not None:
            str += f'{current.value},'
            current = current.next
        str += ']'
        return str


    def contains(self, value):
        last = self.head
        while (last):
            if value == last.value:
                return True
            else:
                last = last.next;
        return False

    def push(self, value):
        newelem = Node(value)
        if self.head is None:
            self.head = newelem
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = newelem

    def get(self, index):
        last = self.head
        el_index = 0
        while el_index <= index:
            if el_index == index:
                return last.value
            el_index = el_index + 1
            last = last.next

    def remove(self, value):
        current = self.head
        if current is not None:
            if current.value == value:
                self.head = current.next
                return
        while current is not None:
            if current.value == value:
                break
            last = current
            current = current.next
        if current == None:
            return
        last.next = current.next

    def printList(self):
        current = self.head
        while current is not None:
            print(current.value,end=' ')
            current = current.next