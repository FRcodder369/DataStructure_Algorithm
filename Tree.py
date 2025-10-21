
root = int(input('Enter the root: '))

class Tree:
    root = root
    root_leftChild = None
    root_rightChild = None
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


        if value < root:
            if Tree.root_leftChild is None:
                Tree.root_leftChild = value

            else:
                currentNode = root
                while True:
                    if value < currentNode:
                        if currentNode.leftChild is None:
                            self.leftChild = value
                            break
                        else:
                            currentNode = currentNode.leftChild




        elif value > root:
            if Tree.root_rightChild is None:
                Tree.root_rightChild = value

            else:
                currentNode = root
                while True:
                    if value > currentNode:
                        if currentNode.rightChild is None:
                            self.rightChild = value
                            break
                        else:
                            currentNode = currentNode.rightChild
