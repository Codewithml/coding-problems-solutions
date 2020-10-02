import unittest
from hashmap import HashTable


class TestHashMap(unittest.TestCase):

    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'first')
        self.assertEqual(hash_table.get(0), 'first')
        hash_table.set(1, 'second')
        self.assertEqual(hash_table.get(1), 'second')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'third')
        self.assertEqual(hash_table.get(0), 'first')
        self.assertEqual(hash_table.get(10), 'third')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'fourth')
        self.assertEqual(hash_table.get(0), 'first')
        self.assertEqual(hash_table.get(10), 'fourth')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        self.assertEqual(hash_table.get(0), 'first')
        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == "__main__":
    main()
