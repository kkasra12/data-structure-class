class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    def __str__(self):
        return f"Node(data={self.data})"

    def __repr__(self):
        return str(self)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        self.__lastNode = self.head
        return self

    def __next__(self):
        if self.__lastNode is None:
            raise StopIteration
        t = self.__lastNode
        self.__lastNode = self.__lastNode.next
        return t

    def __str__(self):
        return " --> ".join([str(i) for i in self])

    def __repr__(self):
        return str(self)

    def lastNode(self):
        if self.head is not None:
            for i in self:
                pass
            return i

    def append(self, newNode):
        if not isinstance(newNode, Node):
            newNode = Node(newNode)
        if self.head:
            self.lastNode().next = newNode
        else:
            self.head = newNode

    def insert(self, newNode, index):
        if not isinstance(newNode, Node):
            newNode = Node(newNode)
        for index_, node in enumerate(self):
            if index_ == index:
                newNode.next = node.next
                node.next = newNode
                break

    def delete(self, index):
        for index_, node in enumerate(self):
            if index_ == index - 1:
                node.next = node.next.next
                break

    def change_head(self, newNode):
        newNode.next = self.head
        self.head = newNode
