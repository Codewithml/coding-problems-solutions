import unittest
from pizzaSlices import PizzaSlices


class TestPizaaSlices(unittest.TestCase):
    def testPizzaSlices(self, func):
        self.assertEqual(func(None, None), None)
        self.assertEqual(func([{'name': 'Joe', 'num': 9},
                         {'name': 'Cami', 'num': 3},
                         {'name': 'Cassidy', 'num': 4}], 8), 2)
        self.assertEqual(func([{'name': 'madLad', 'num': 4},
                         {'name': 'John', 'num': 7},
                         {'name': 'Doe', 'num': 4}], 4), 4),
        self.assertEqual(func([{'name': 'kevin', 'num': 6},
                         {'name': 'joe', 'num': 6},
                         {'name': 'nick', 'num': 5}], 6), 3)
        print("All test cases passed!")


def main():
    test = TestPizaaSlices()
    pizza = PizzaSlices()
    test.testPizzaSlices(pizza.pizzaSlices)


if __name__ == "__main__":
    main()
