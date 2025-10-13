import nodesOfLinkedList as nodes

class LinkedList:
    def __init__(self):
        self.head = nodes.node1
        self.tail = nodes.node4
        self.size = 0

    def traversal(self):
        self.size = 0
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            self.size += 1
            current_node = current_node.next
        print(None)

    def removeFirst(self):
        first = self.head
        new_first = first.next
        self.head = new_first
        self.size -= 1


    def removeLast(self):
        currentNode = self.head
        last = self.tail


        while currentNode != None:
            if currentNode.next == last:
                self.tail = currentNode
                self.tail.next = None
            currentNode = currentNode.next
        self.size -= 1


    def addFirst(self, item):
        new_first = nodes.Node(item)
        new_first.next = self.head
        self.head = new_first
        self.size += 1


    def addLast(self, item):
        new_last = nodes.Node(item)
        self.tail.next = new_last
        self.tail = new_last
        self.size += 1


    def removeItem(self, item):
        currentNode = self.head
        while currentNode != None:
            if currentNode.next == item:
                currentNode.next = currentNode.next.next
                self.size -= 1
                break


    def removeIndex(self, index):
        if 0 < index < self.size:
            self.size -= 1
            pastNode = self.head
            currentNode = pastNode.next
            i = 1
            while i < self.size:
                if i == index:
                    pastNode.next = currentNode.next
                    break
                pastNode = currentNode
                currentNode = currentNode.next
                i += 1
        if index == 0:
            self.removeFirst()
            self.size -= 1


