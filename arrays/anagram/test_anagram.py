import unittest
from anagram import Anagram


class TestAnagram(unittest.TestCase):

    def test_anagram(self, sol):
        self.assertEqual(sol(None, None), None)
        self.assertEqual(sol('go go go', 'gggooo'), True)
        self.assertEqual(sol('abc', 'cba'), True)
        self.assertEqual(sol('hi man', 'hi     man'), True)
        self.assertEqual(sol('aabbcc', 'aabbc'), False)
        self.assertEqual(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


def main():
    test = TestAnagram()
    anagram = Anagram()
    test.test_anagram(anagram.anagram)
    test.test_anagram(anagram.anagram2)


if __name__ == "__main__":
    main()
