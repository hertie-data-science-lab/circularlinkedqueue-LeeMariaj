class Empty(Exception):
    pass


class CircularQueue:
    # Queue implementation using circularly linked list for storage

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._data = []
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        if self._size == 0:
            raise Empty("Queue is empty")
        else:
            node = self._head
            nodes = []
            while node is not None:
                nodes.append(node._element)
                node = node._next
            nodes.append(" -> ")
            nodes.append(self._head._element)
            return " -> ".join(nodes)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty() == True:
            raise Empty("Queue is empty")
        else:
            return (self._head._element)

    def dequeue(self):
        if self._size == 0:
            raise Empty("Queue is empty")

        elif self._size == 1:
            self._head = None
            self._size -= 1
            raise Empty("Queue is empty")

        else:
            self._data.pop(0)
            self._head = self._data[0]
            self._size -= 1

    def enqueue(self, e):
        node = self._Node(e, None)
        self._size += 1
        if self._head == None:
            self._head = node
            self._tail = node
            self._data.append(node)
        else:
            self._data[-1]._next = node
            self._tail = node
            self._data.append(node)

    def rotate(self):
        node = self._head
        self._head = None
        nodes = []
        while node is not None:
            nodes.append(node._element)
            node = node._next
        for i in range(len(nodes)):
            j = (len(nodes) - 1) - i
            self.enqueue(nodes[j])