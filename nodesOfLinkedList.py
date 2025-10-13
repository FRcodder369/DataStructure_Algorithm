

class Nodes:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Nodes(1)
node2 = Nodes(2)
node3 = Nodes(3)
node4 = Nodes(4)

node1.next = node2
node2.next = node3
node3.next = node4
