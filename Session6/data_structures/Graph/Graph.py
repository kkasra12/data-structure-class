class Graph:
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_node(self, node):
        self.V.add(node)

    def add_nodes(self, *args):
        for i in args:
            self.add_node(i)

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if not (node2, node1) in self.E:
            self.E.add((node1, node2))

    def is_connected(self, node1, node2):
        return (node1, node2) in self.E or (node2, node1) in self.E

    def __str__(self):
        return f"G(V:{self.V},\n  E:{self.E})"

    def __repr__(self):
        return str(self)
