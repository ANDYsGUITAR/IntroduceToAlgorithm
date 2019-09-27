class Queue(object):
    def __init__(self, n):
        self.size = n
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def enqueue(self, val):
        if len(self.data) == self.size:
            print("The queue is full")
            return None
        self.data.append(val)

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return None
        return self.data.pop(0)

q = Queue(2)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())

