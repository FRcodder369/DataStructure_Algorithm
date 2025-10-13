# FIFO

class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, value):
        new_queue = []
        if self.size != 0:
            new_queue.append(value)
            self.size += 1
            for x in self.queue:
                new_queue.append(x)
                self.size += 1
            self.queue = new_queue
        else:
            self.queue.append(value)
            self.size += 1


    def dequeue(self):
        self.queue = self.queue[1:]

    def peek(self):
        if self.size != 0:
            return self.queue[0]

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
