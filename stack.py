# LIFO
class Stack:
    def __init__(self):
        array = []
        size = 0

    def add(self, item):
        self.array += [item]
        self.size += 1

    def pop(self):
        x = self.array[-1]
        self.array = self.array[:-1]
        self.size -= 1
        return x

    def peek(self):
        x = self.array[-1]
        return x

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

