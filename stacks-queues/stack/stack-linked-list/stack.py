class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def __len__(self):
        curr = self.top
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        self.top = Node(data, self.top)

    def peek(self):
        return self.top.data if self.top is not None else None

    def isEmpty(self):
        return self.peek() is None
