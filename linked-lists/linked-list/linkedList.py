class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def insertStart(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def insertEnd(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def search(self, data):
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node.data
            curr_node = curr_node.next
        return None

    def remove(self, data):
        if data is None:
            return None
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def remove2(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        curr_node = self.head
        if curr_node.data == data:
            curr_node = curr_node.next
            return
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def printList(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def getData(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data
