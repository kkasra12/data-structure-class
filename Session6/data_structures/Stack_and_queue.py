from .LinkedList import LinkedList, Node


class Stack:
    def __init__(self):
        self.stack = LinkedList()
        self.len = 0

    def push(self, item):
        self.stack.change_head(Node(item))
        self.len += 1

    def pop(self):
        lastNode = self.stack.head.data
        #         self.stack.changeHead(self.stack.head.next)
        self.stack.head = self.stack.head.next
        self.len -= 1
        return lastNode

    def last(self):
        return self.stack.head.data

    def __len__(self):
        return self.len

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self)


class Queue:
    def __init__(self):
        self.head = None  # enqueue
        self.tail = None  # dequeue
        self.len = 0

    def __len__(self):
        return self.len

    def enqueue(self, x):
        if self.len == 0:
            self.head = Node(x)
            self.tail = self.head
            self.len = 1
            return
        self.head.next = Node(x)
        self.head = self.head.next

    def dequeue(self):
        if self.len == 0:
            return
        resp = self.tail
        self.tail = self.tail.next
        self.len -= 1
        return resp
