import unittest
from deque import Deque


class TestDeque(unittest.TestCase):
    def testDeque(self):
        print('Test: Empty Deque')
        deque = Deque()
        self.assertEqual(deque.size(), 0)
        self.assertEqual(deque.getFront(), None)
        self.assertEqual(deque.getRear(), None)
        self.assertEqual(deque.removeFront(), None)
        self.assertEqual(deque.removeRear(), None)
        self.assertEqual(deque.isEmpty(), True)

        print('Test: One element')
        deque = Deque()
        deque.addFront(5)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.getFront(), 5)
        self.assertEqual(deque.removeFront(), 5)
        self.assertEqual(deque.isEmpty(), True)
        deque.addRear(5)
        self.assertEqual(deque.isEmpty(), False)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.getRear(), 5)
        self.assertEqual(deque.removeRear(), 5)
        self.assertEqual(deque.isEmpty(), True)

        print('Test: Multiple elements')
        deque = Deque()
        deque.addFront(1)
        deque.addRear(3)
        deque.addFront(2)
        deque.addRear(4)
        self.assertEqual(deque.size(), 4)
        self.assertEqual(deque.getFront(), 2)
        self.assertEqual(deque.removeFront(), 2)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.removeRear(), 4)
        self.assertEqual(deque.getRear(), 3)
        self.assertEqual(deque.size(), 2)
        self.assertEqual(deque.isEmpty(), False)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.removeRear(), 3)
        self.assertEqual(deque.isEmpty(), True)
        print('Success: testDeque')


def main():
    test = TestDeque()
    test.testDeque()


if __name__ == "__main__":
    main()
