import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def testEnqueue(self):
        print('Test: Enqueue on an empty queue')
        qu = Queue()
        qu.enqueue(1)
        self.assertEqual(qu.getData(), [1])

        print('Test: Enqueue on a non-empty queue')
        qu = Queue()
        qu.enqueue(2)
        qu.enqueue(3)
        self.assertEqual(qu.getData(), [2, 3])
        print('Success: enqueue')

    def testDequeue(self):
        print('Test: Dequeue on an empty queue')
        qu = Queue()
        self.assertEqual(qu.dequeue(), None)

        print('Test: Dequeue on a non-empty queue')
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(3)
        qu.enqueue(5)
        self.assertEqual(qu.dequeue(), 1)
        self.assertEqual(qu.dequeue(), 3)
        self.assertEqual(qu.dequeue(), 5)

        print('Success: testDequeue') 


def main():
    test = TestQueue()
    test.testEnqueue()
    test.testDequeue()


if __name__ == "__main__":
    main()
