import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def fizz_buzz_solution(self):
        fizzbuzz = FizzBuzz()
        self.assertRaises(TypeError, fizzbuzz.fizzbuzz, None)
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(fizzbuzz.fizzbuzz(15), expected)
        print("Success: test_fizz_buzz")


def main():
    test = TestFizzBuzz()
    test.fizz_buzz_solution()


if __name__ == "__main__":
    main()
