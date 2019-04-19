from .node import Node

class PriorityQueue(object):
    def __init__(self):
        self._head = None
        self._count = 0

    @property
    def count(self):
        return self._count
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            previous = None
            while current and self._compare(current.value, new_node.value):
                previous = current
                current = current.next_node
            if current is not None:
                new_node.next_node = current
            if previous is not None:
                previous.next_node = new_node
            else:
                self._head = new_node

        self._count +=1

    def dequeue(self):
        if self._head:
            temp = self._head
            self._head = self._head.next_node
            self._count -=1
            return temp.value
        return None
    
    def _compare(self, value1, value2):
        return value1 < value2

    def __str__(self):
        current = self._head
        str = ''
        while current is not None:
            str += f'{current.value} ->' 
            current = current.next_node
        return str
    