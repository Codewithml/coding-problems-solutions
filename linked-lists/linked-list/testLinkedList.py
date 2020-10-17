import unittest
from linkedList import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def testInsertStart(self):
        print('Test: insertStart on an empty linked list')
        linkedList = LinkedList(None)
        linkedList.insertStart(1)
        self.assertEqual(linkedList.getData(), [1])

        print('Test: insertStart on a None')
        linkedList.insertStart(None)
        self.assertEqual(linkedList.getData(), [1])

        print('Test: insertStart on a non-empty linked list')
        linkedList.insertStart(11)
        linkedList.insertStart('letters')
        self.assertEqual(linkedList.getData(), ['letters', 11, 1])

        print('Success: testInsertStart')

    def testInsertEnd(self):
        print('Test: insertLast on an empty linked list')
        linkedList = LinkedList(None)
        linkedList.insertEnd(2)
        self.assertEqual(linkedList.getData(), [2])

        print('Test: insertEnd a None')
        linkedList.insertEnd(None)
        self.assertEqual(linkedList.getData(), [2])

        print('Test: insertEnd on a non-empty linked list')
        linkedList.insertEnd('4')
        linkedList.insertEnd(6)
        self.assertEqual(linkedList.getData(), [2, '4', 6])

        print('Success: insertEnd')

    def testSearch(self):
        print('Test: Search on an empty linked list')
        linkedList = LinkedList(None)
        element = linkedList.search(1)
        self.assertEqual(element, None)

        print('Test: Search on a None')
        linkedList1 = LinkedList(10)
        element = linkedList1.search(None)
        self.assertEqual(element, None)

        print('Test: Search on a non-empty linked list')
        head = Node(10)
        linkedList2 = LinkedList(head)
        linkedList2.insertStart(9)
        linkedList2.insertStart(8)
        linkedList2.insertStart(7)
        linkedList2.insertEnd(11)
        element = linkedList2.search(11)
        element2 = linkedList2.search('aaa')
        self.assertEqual(element, 11)
        self.assertEqual(element2, None)
        print('Success: testSearch')

    def testRemove(self):
        print('Test: remove element from an empty linked list')
        linkedList = LinkedList(None)
        linkedList.remove(2)
        self.assertEqual(linkedList.getData(), [])

        print('Test: remove a None')
        head = Node(1)
        linkedList = LinkedList(head)
        linkedList.remove(None)
        self.assertEqual(linkedList.getData(), [1])

        print('Test: remove element from a non-empty linked list')
        head = Node(1)
        linkedList = LinkedList(head)
        linkedList.insertEnd(2)
        linkedList.insertEnd(3)
        linkedList.insertStart(0)
        linkedList.remove(0)
        linkedList.remove2(2)
        self.assertEqual(linkedList.getData(), [1, 3])
        linkedList.remove('abc')
        self.assertEqual(linkedList.getData(), [1, 3])

        print('Success: testRemove')

    def testLen(self):
        print('Test length of thean empty linked list')
        linkedList = LinkedList(None)
        self.assertEqual(len(linkedList), 0)

        print('Test length of non empty linked list')
        head = Node(0)
        linkedList = LinkedList(head)
        linkedList.insertStart(1)
        linkedList.insertStart(2)
        linkedList.insertEnd(3)
        self.assertEqual(len(linkedList), 4)

        print('Success: testLen')


def main():
    test = TestLinkedList()
    test.testInsertStart()
    test.testInsertEnd()
    test.testSearch()
    test.testRemove()
    test.testLen()


if __name__ == "__main__":
    main()
