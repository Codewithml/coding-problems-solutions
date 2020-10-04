class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if self.isEmpty():
            return None
        print(self.items)
        return self.items.pop()

    def size(self):
        return len(self.items)
