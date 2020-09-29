'''
Given an array of people objects (where each person has a name
and a number of pizza
slices they’re hungry for) and a number for the number of slices
that the pizza can be sliced into, return the number of pizzas
you need to buy.

$ arr = [{ name: Joe, num: 9 }, { name: Cami, num: 3 },
{ name: Cassidy, num: 4 }]
$ gimmePizza(arr, 8)
$ 2 // 16 slices needed, pizzas can be sliced into 8 pieces,
so 2 pizzas should be ordered
'''
import math


class PizzaSlices(object):
    def pizzaSlices(self, arr, sliced):
        if arr is None or sliced is None:
            return None
        count = 0
        for i, slices in enumerate(num['num'] for num in arr):
            count += slices
        return math.ceil(count / sliced)
