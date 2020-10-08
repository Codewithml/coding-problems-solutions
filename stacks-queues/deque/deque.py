class Deque(object):
    def __init__(self):
        self.deque = []

    def isEmpty(self):
        return self.deque == []

    def addRear(self, data):
        self.deque.insert(0, data)

    def addFront(self, data):
        self.deque.append(data)

    def getRear(self):
        if self.isEmpty():
            return None
        return self.deque[0]

    def getFront(self):
        if self.isEmpty():
            return None
        return self.deque[-1]

    def removeRear(self):
        if self.isEmpty():
            return None
        return self.deque.pop(0)

    def removeFront(self):
        if self.isEmpty():
            return None
        return self.deque.pop()

    def size(self):
        return len(self.deque)
